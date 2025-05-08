from repositories.contact_repository import ContactRepository
from use_cases.public.contact.create_contact.create_contact_dto import CreateContactDTO
from use_cases.public.contact.create_contact.create_contact_use_case import CreateContactUseCse
from fastapi import Request, Response, APIRouter

router = APIRouter()

contact_repository = ContactRepository()
create_contact_use_case = CreateContactUseCse(contact_repository)

@router.post("/contact/create")
def create_contact(create_contact_dto: CreateContactDTO, response: Response, request: Request):
    return create_contact_use_case.execute(create_contact_dto, response, request)