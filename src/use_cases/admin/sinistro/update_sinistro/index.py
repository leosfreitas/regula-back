from use_cases.admin.sinistro.update_sinistro.update_sinistro_use_case import UpdateSinistroUseCase
from use_cases.admin.sinistro.update_sinistro.update_sinistro_dto import UpdateSinistroDTO
from repositories.sinistro_repository import SinistroRepository
from fastapi import Request, Response, APIRouter, Depends
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

sinistro_repository = SinistroRepository()
update_sinistro_use_case = UpdateSinistroUseCase(sinistro_repository)

@router.put("/admin/update/sinistro/{sinistro_id}", dependencies=[Depends(validade_admin_auth_token)])
async def update_sinistro(sinistro_id: str, dto: UpdateSinistroDTO, request: Request, response: Response):
    return update_sinistro_use_case.execute(request, response, sinistro_id, dto)