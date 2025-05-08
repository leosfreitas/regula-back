from repositories.contact_repository import ContactRepository
from fastapi import Request, Response

class DeleteContactUseCase:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def execute(self, request: Request, response: Response, contact_id: str) -> None:
        """
        Use case to delete a contact by its ID.
        :param request: The HTTP request object.
        :param response: The HTTP response object.
        :param contact_id: The ID of the contact to be deleted.
        """
        self.contact_repository.delete_contact(contact_id)
        return Response(status_code=204)  