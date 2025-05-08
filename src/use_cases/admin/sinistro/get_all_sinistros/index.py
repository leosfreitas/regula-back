from repositories.sinistro_repository import SinistroRepository
from use_cases.admin.sinistro.get_all_sinistros.get_all_sinistros_use_case import GetAllSinistros
from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

get_all_sinistros_use_case = GetAllSinistros(SinistroRepository)

@router.get("/admin/get/sinistros", dependencies=[Depends(validade_admin_auth_token)])
async def get_all_sinistros(request: Request, response: Response):
    return get_all_sinistros_use_case.execute(response, request)