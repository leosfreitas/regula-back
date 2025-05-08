from repositories.sinistro_repository import SinistroRepository
from fastapi import Request, Response

class GetAllSinistros: 
    def __init__(self, sinistro_repository: SinistroRepository) -> None:
        self.sinistro_repository = sinistro_repository

    def execute(self, response: Response, request: Request):
        sinistros = self.sinistro_repository.get_all_sinistros(self)
        response.status_code = 200

        return {"status": "success", "sinistros": sinistros}
