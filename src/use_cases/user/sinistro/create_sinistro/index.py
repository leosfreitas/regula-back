from repositories.sinistro_repository import SinistroRepository    
from use_cases.user.sinistro.create_sinistro.create_sinistro_dto import CreateSinistroDTO
from use_cases.user.sinistro.create_sinistro.create_sinistro_use_case import CreateSinistroUseCase
from fastapi import Request, Response, APIRouter, Depends
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()

sinistro_repository = SinistroRepository()
create_sinistro_use_case = CreateSinistroUseCase(sinistro_repository)

@router.post("/user/sinistro/create", dependencies=[Depends(validade_user_auth_token)])
def create_sinistro(create_sinistro_dto: CreateSinistroDTO, response: Response, request: Request):
    return create_sinistro_use_case.execute(create_sinistro_dto, response, request)