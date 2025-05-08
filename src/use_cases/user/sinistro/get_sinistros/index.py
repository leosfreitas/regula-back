from repositories.sinisitro_repository import SinistroRepository
from use_cases.user.sinistro.get_sinistros.get_sinistros_use_case import GetSinistrosUseCase
from fastapi import APIRouter, Depends, Request, Response
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()
repo = SinistroRepository()
use_case = GetSinistrosUseCase(SinistroRepository())

@router.get("/user/get/sinistros", dependencies=[Depends(validade_user_auth_token)])
async def get_sinistros(request: Request, response: Response):
    return use_case.execute(response, request)