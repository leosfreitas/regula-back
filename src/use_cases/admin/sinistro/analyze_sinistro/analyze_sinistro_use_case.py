from repositories.sinistro_repository import SinistroRepository
from fastapi import Response
from bson import ObjectId
from use_cases.admin.sinistro.analyze_sinistro.classify import classify_claim

class AnalyzeSinistroUseCase:
    def __init__(self, sinistro_repository: SinistroRepository) -> None:
        self.sinistro_repository = sinistro_repository

    def convert_field_names(self, sinistro_dict: dict) -> dict:
        field_mapping = {
            'accident_area': 'AccidentArea',
            'sex': 'Sex',
            'fault': 'Fault',
            'police_report_filed': 'PoliceReportFiled',
            'witness_present': 'WitnessPresent',
            'agent_type': 'AgentType',
            'vehicle_price': 'VehiclePrice',
            'age_of_vehicle': 'AgeOfVehicle',
            'base_policy': 'BasePolicy',
            'age': 'Age',
            'make': 'Make',
            'marital_status': 'MaritalStatus',
            'policy_type': 'PolicyType',
            'vehicle_category': 'VehicleCategory',
            'deductible': 'Deductible',
            'days_policy_accident': 'Days_Policy_Accident',
            'days_policy_claim': 'Days_Policy_Claim',
            'past_number_of_claims': 'PastNumberOfClaims',
            'age_of_policy_holder': 'AgeOfPolicyHolder',
            'number_of_cars': 'NumberOfCars'
        }
        
        converted_dict = {}
        for snake_case_key, pascal_case_key in field_mapping.items():
            if snake_case_key in sinistro_dict:
                converted_dict[pascal_case_key] = sinistro_dict[snake_case_key]
        
        return converted_dict

    def execute(self, sinistro_id: str, response: Response) -> dict:
        sinistro = self.sinistro_repository.get_sinistro_by_id(self, sinistro_id)

        if not sinistro:
            response.status_code = 404
            return {"status": "error", "message": "Sinistro não encontrado"}

        sinistro_dict = sinistro.to_mongo().to_dict()

        for field in ['_id', 'user_id', 'status']:
            sinistro_dict.pop(field, None)

        converted_sinistro = self.convert_field_names(sinistro_dict)
        novo_status = classify_claim(converted_sinistro)

        self.sinistro_repository.update_status(self, sinistro_id, novo_status)
        
        response.status_code = 200
        return {"status": "success", "resultado": novo_status}