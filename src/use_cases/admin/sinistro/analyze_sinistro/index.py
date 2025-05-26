from repositories.sinistro_repository import SinistroRepository
from use_cases.admin.sinistro.analyze_sinistro.analyze_sinistro_use_case import AnalyzeSinistroUseCase
from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

analyze_sinistro_use_case = AnalyzeSinistroUseCase(SinistroRepository)

@router.post("/admin/sinistro/analyze/{sinistro_id}", dependencies=[Depends(validade_admin_auth_token)])
async def analyze_sinistro(sinistro_id: str, request: Request, response: Response):
    return analyze_sinistro_use_case.execute(sinistro_id, response)