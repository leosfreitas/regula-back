from repositories.contact_repository import ContactRepository
from fastapi import Response, Request, Depends, APIRouter
from use_cases.admin.contact.delete_contact.delete_contact_use_case import DeleteContactUseCase
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()
delete_contact_use_case = DeleteContactUseCase(ContactRepository())

@router.delete("/admin/contact/delete/{contact_id}", dependencies=[Depends(validade_admin_auth_token)])
def delete_contact(contact_id: str, response: Response, request: Request):
    return delete_contact_use_case.execute(request, response, contact_id)