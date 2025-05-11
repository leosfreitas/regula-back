from repositories.contact_repository import ContactRepository
from use_cases.admin.contact.update_contact.update_contact_dto import UpdateContactDTO
from fastapi import Request, Response

class UpdateContactUseCase():
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def execute(self, request: Request, response: Response, contact_id: str, dto: UpdateContactDTO):
        status = dto.status

        updated_contact = self.contact_repository.update_status(contact_id, status)

        if not updated_contact:
            response.status_code = 404
            return {"error": "Contact not found"}

        response.status_code = 200
        return updated_contact