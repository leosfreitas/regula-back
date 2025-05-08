from repositories.contact_repository import ContactRepository
from use_cases.admin.contact.get_contacts.get_contacts_use_case import GetContactsUseCase
from fastapi import APIRouter, Depends, Request, Response
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()
repo = ContactRepository()
use_case = GetContactsUseCase(ContactRepository())

@router.get("/admin/get/contacts", dependencies=[Depends(validade_admin_auth_token)])
async def get_contacts(request: Request, response: Response):
    return use_case.execute(response, request)