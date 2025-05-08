from repositories.contact_repository import ContactRepository
from fastapi import Response, Request

class GetContactsUseCase:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def execute(self, response: Response, request: Request) -> dict:
        
        response.status_code = 200
        
        contacts = self.contact_repository.get_all_contacts()

        return {"status": "success", "contacts": contacts}