from repositories.sinistro_repository import SinistroRepository    
from use_cases.user.sinistro.create_sinistro.create_sinistro_dto import CreateSinistroDTO
from utils.get_session_info import *
from fastapi import Request, Response
from entities.sinistro import Sinistro

class CreateSinistroUseCase:
    sinistro_repository = SinistroRepository

    def __init__(self, sinistro_repository: SinistroRepository):
        self.sinistro_repository = sinistro_repository

    def execute(self, create_sinistro_dto: CreateSinistroDTO, response: Response, request: Request):
        user_id = get_user_id(request)
        past_number_of_claims = len(self.sinistro_repository.get_sinistros_by_user_id(user_id))

        sinistro_data = Sinistro(
            user_id=user_id,
            status="Aberto",
            
            accident_area=create_sinistro_dto.accident_area,
            sex=create_sinistro_dto.sex,
            age=create_sinistro_dto.age,
            fault=create_sinistro_dto.fault,
            police_report_filed=create_sinistro_dto.police_report_filed,
            witness_present=create_sinistro_dto.witness_present,
            agent_type=create_sinistro_dto.agent_type,
            vehicle_price=create_sinistro_dto.vehicle_price,
            age_of_vehicle=create_sinistro_dto.age_of_vehicle,
            base_policy=create_sinistro_dto.base_policy,
            make=create_sinistro_dto.make,
            marital_status=create_sinistro_dto.marital_status,
            policy_type=create_sinistro_dto.policy_type,
            vehicle_category=create_sinistro_dto.vehicle_category,
            deductible=create_sinistro_dto.deductible,
            days_policy_accident=create_sinistro_dto.days_policy_accident,
            days_policy_claim=create_sinistro_dto.days_policy_claim,
            past_number_of_claims=past_number_of_claims,
            age_of_policy_holder=create_sinistro_dto.age_of_policy_holder,
            number_of_cars=create_sinistro_dto.number_of_cars,
        )

        sinistro = self.sinistro_repository.save(user_id, sinistro_data)

        response.status_code = 201
        return {"status": "success", "message": "Sinistro criado com sucesso", "sinistro_id": str(sinistro.id)}