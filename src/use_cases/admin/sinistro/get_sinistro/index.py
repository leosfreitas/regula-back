from repositories.sinistro_repository import SinistroRepository
from use_cases.admin.sinistro.get_sinistro.get_sinistro_use_case import GetSinistroUseCase
from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

get_all_sinistros_use_case = GetSinistroUseCase(SinistroRepository)

@router.get("/admin/get/sinistros/{user_id}", dependencies=[Depends(validade_admin_auth_token)])
async def get_all_sinistros(user_id: str, request: Request, response: Response):
    return get_all_sinistros_use_case.execute(user_id, response)