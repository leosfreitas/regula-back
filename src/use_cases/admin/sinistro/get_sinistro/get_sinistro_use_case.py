from repositories.sinisitro_repository import SinistroRepository
from fastapi import Response

class GetSinistroUseCase:
    def __init__(self, sinistro_repository: SinistroRepository) -> None:
        self.sinistro_repository = sinistro_repository

    def execute(self, user_id: str, response: Response) -> dict:
        """
        Get all sinistros for a given user_id (admin access).
        """
        sinistros = self.sinistro_repository.get_sinistros_by_user_id(self, user_id)

        response.status_code = 200
        return {"status": "success", "sinistros": sinistros}
