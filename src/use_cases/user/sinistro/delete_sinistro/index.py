from repositories.sinistro_repository import SinistroRepository
from fastapi import Request, Response, Depends, APIRouter
from use_cases.user.sinistro.delete_sinistro.delete_sinistro_use_case import DeleteSinistroUseCase
from middlewares.validate_user_auth_token import validade_user_auth_token

router = APIRouter()
delete_sinistro_use_case = DeleteSinistroUseCase(SinistroRepository())

@router.delete("/user/sinistro/delete/{sinistro_id}", dependencies=[Depends(validade_user_auth_token)])
def delete_sinistro(sinistro_id: str, response: Response, request: Request):
    return delete_sinistro_use_case.execute(request, response, sinistro_id)
