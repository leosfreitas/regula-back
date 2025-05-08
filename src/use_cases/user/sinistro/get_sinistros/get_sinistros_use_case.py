from repositories.sinisitro_repository import SinistroRepository
from utils.get_session_info import get_user_id
from fastapi import Response, Request

class GetSinistrosUseCase:
    def __init__(self, sinistro_repository: SinistroRepository):
        self.sinistro_repository = sinistro_repository

    def execute(self, response: Response, request: Request) -> dict:
        
        user_id = get_user_id(request)

        response.status_code = 200
        
        sinistros = self.sinistro_repository.get_sinistros_by_user_id(user_id)

        return {"status": "success", "sinistros": sinistros}
    