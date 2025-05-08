from repositories.sinistro_repository import SinistroRepository    
from use_cases.user.sinistro.create_sinistro.create_sinistro_dto import CreateSinistroDTO
from utils.get_session_info import *
from fastapi import Request, Response
from entities.sinistro import Sinistro
from datetime import datetime 

class CreateSinistroUseCase:
    sinistro_repository = SinistroRepository

    def __init__(self, sinistro_repository: SinistroRepository):
        self.sinistro_repository = sinistro_repository

    def execute(self, create_sinistro_dto: CreateSinistroDTO, response: Response, request: Request):
        user_id = get_user_id(request)

        if not create_sinistro_dto.cnh or not create_sinistro_dto.cpf or not create_sinistro_dto.endereco or not create_sinistro_dto.data_acidente or not create_sinistro_dto.descricao:
            response.status_code = 406
            return {"status": "error", "message": " Sinistro não criado, pois falta informações"}

        

        sinistro_data = Sinistro(
            status="Aberto",
            data=datetime.now(),
            cnh=create_sinistro_dto.cnh,
            cpf=create_sinistro_dto.cpf,
            endereco=create_sinistro_dto.endereco,
            data_acidente=create_sinistro_dto.data_acidente,
            descricao=create_sinistro_dto.descricao,
            user_id=user_id
        )


        sinistro = self.sinistro_repository.create_sinistro(user_id, sinistro_data)

        response.status_code = 201
        return {"status": "success", "message": "Sinistro criado com sucesso", "sinistro": sinistro}
