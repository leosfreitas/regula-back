from repositories.sinistro_repository import SinistroRepository
from use_cases.admin.sinistro.update_sinistro.update_sinistro_dto import UpdateSinistroDTO
from fastapi import Request, Response

class UpdateSinistroUseCase():
    def __init__(self, sinistro_repository: SinistroRepository):
        self.sinistro_repository = sinistro_repository

    def execute(self, request: Request, response: Response, sinistro_id: str, dto: UpdateSinistroDTO):
        status = dto.status

        updated_sinistro = self.sinistro_repository.update_status(sinistro_id, status)

        if not updated_sinistro:
            response.status_code = 404
            return {"error": "Sinistro not found"}

        response.status_code = 200
        return updated_sinistro