from repositories.contact_repository import ContactRepository
from use_cases.public.contact.create_contact.create_contact_dto import CreateContactDTO
from entities.contact import Contact
from fastapi import Request, Response

class CreateContactUseCse:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def execute(self, create_contact_dto: CreateContactDTO, response: Response, request: Request):

        if not create_contact_dto:
            response.status_code = 406
            return {"status": "error", "message": "Informações faltando"}
        
        contact_data = Contact(
            nome = create_contact_dto.nome,
            email = create_contact_dto.email,
            telefone = create_contact_dto.telefone,
            empresa = create_contact_dto.empresa, 
            mensagem = create_contact_dto.mensagem,
            status = "N",
        )

        contact = self.contact_repository.save(contact_data)

        response.status_code = 201 
        return {"status": "success", "message": "Contato criado com sucesso", "contato": contact}