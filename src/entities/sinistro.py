import dotenv
from pydantic import BaseModel
from typing import Literal
from datetime import datetime
dotenv.load_dotenv()

class Sinistro(BaseModel):
    _id: str
    user_id: str
    status: Literal["Aberto", "Análise Manual Necessária", "Negado", "Aprovado"]
    accident_area: Literal["Urban", "Rural"]
    sex: Literal["Male", "Female"]
    fault: Literal["Policy Holder", "Third Party"]
    police_report_filed: Literal["Yes", "No"]
    witness_present: Literal["Yes", "No"]
    agent_type: Literal["External", "Internal"]
    vehicle_price: Literal["less than 20000", "20000 to 29000", "30000 to 39000", "40000 to 59000", "60000 to 69000", "more than 69000"]
    age_of_vehicle: Literal["new", "2 years", "3 years", "4 years", "5 years", "6 years", "7 years", "more than 7"]
    base_policy: Literal["Liability", "Collision", "All Perils"]
    age: int
    make: str
    marital_status: Literal["Single", "Married", "Widow", "Divorced"]
    policy_type: Literal["Sedan - All Perils", "Sedan - Collision", "Sport - Collision", "Utility - All Perils", "Utility - Collision", "Sedan - Liability"]
    vehicle_category: Literal["Sedan", "Sport", "Utility"]
    deductible: int
    days_policy_accident: Literal["none", "1 to 7", "8 to 15", "15 to 30", "more than 30"]
    days_policy_claim: Literal["none", "1 to 7", "8 to 15", "15 to 30", "more than 30"]
    past_number_of_claims: int
    age_of_policy_holder: int
    number_of_cars: int