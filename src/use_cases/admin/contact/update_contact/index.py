from repositories.contact_repository import ContactRepository
from use_cases.admin.contact.update_contact.update_contact_dto import UpdateContactDTO
from use_cases.admin.contact.update_contact.update_contact_use_case import UpdateContactUseCase
from fastapi import Request, Response, APIRouter, Depends
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

contact_repository = ContactRepository()
update_contact_use_case = UpdateContactUseCase(contact_repository)

@router.put("/admin/update/contact/{contact_id}", dependencies=[Depends(validade_admin_auth_token)])
async def update_contact(contact_id: str, dto: UpdateContactDTO, request: Request, response: Response):
    return update_contact_use_case.execute(request, response, contact_id, dto)