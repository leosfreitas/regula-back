from repositories.sinistro_repository import SinistroRepository
from fastapi import Request, Response

class DeleteSinistroUseCase:
    def __init__(self, sinistro_repository: SinistroRepository):
        self.sinistro_repository = sinistro_repository

    def execute(self, request: Request, response: Response, sinistro_id: str) -> None:
        """
        Use case to delete a sinistro by its ID.
        :param request: The HTTP request object.
        :param response: The HTTP response object.
        :param sinistro_id: The ID of the sinistro to be deleted.
        """
        self.sinistro_repository.delete_sinistro(sinistro_id)
        return Response(status_code=204) 