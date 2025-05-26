from repositories.sinistro_repository import SinistroRepository
from fastapi import Response
from bson import ObjectId

class AnalyzeSinistroUseCase:
    def __init__(self, sinistro_repository: SinistroRepository) -> None:
        self.sinistro_repository = sinistro_repository

    def execute(self, sinistro_id: str, response: Response) -> dict:
        """
        Get all sinistros for a given sinistro_id (admin access),
        excluding internal fields from the response.
        """
        sinistro = self.sinistro_repository.get_sinistro_by_id(sinistro_id)

        if not sinistro:
            response.status_code = 404
            return {"status": "error", "message": "Sinistro não encontrado"}

        sinistro_dict = sinistro.to_mongo().to_dict()

        for field in ['_id', 'user_id', 'status']:
            sinistro_dict.pop(field, None)

        ### modelo do que seria.

        modelo = "RODANDO O MODELO DE IA"

        status = "RESPOSTA DO MODELO"

        updated_sinistro = self.sinistro_repository.update_status(sinistro_id, status)
        
        response.status_code = 200
        return {"status": "success", "sinistro": sinistro_dict}