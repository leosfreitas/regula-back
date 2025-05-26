from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class SinistroModel(Document):  
    sensitivity_fields = []

    user_id = StringField(required=True)
    status = StringField(required=True, choices=["Aberto", "Em análise", "Negado", "Aprovado", "Pago"])
    accident_area = StringField(required=True, choices=["Urban", "Rural"])
    sex = StringField(required=True, choices=["Male", "Female"])
    fault = StringField(required=True, choices=["Policy Holder", "Third Party"])
    police_report_filed = StringField(required=True, choices=["Yes", "No"])
    witness_present = StringField(required=True, choices=["Yes", "No"])
    agent_type = StringField(required=True, choices=["External", "Internal"])
    vehicle_price = StringField(required=True, choices=["less than 20000", "20000 to 29000", "30000 to 39000", "40000 to 59000", "60000 to 69000", "more than 69000"])
    age_of_vehicle = StringField(required=True, choices=["new", "2 years", "3 years", "4 years", "5 years", "6 years", "7 years", "more than 7"])
    base_policy = StringField(required=True, choices=["Liability", "Collision", "All Perils"])
    age = IntField(required=True, min_value=17)
    make = StringField(required=True)
    month_claimed = StringField(required=True, choices=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    marital_status = StringField(required=True, choices=["Single", "Married", "Widow", "Divorced"])
    policy_type = StringField(required=True)
    vehicle_category = StringField(required=True, choices=["Sedan", "Sport", "Utility"])
    deductible = IntField(required=True)
    days_policy_accident = StringField(required=True, choices=["none", "1 to 7", "8 to 15", "15 to 30", "more than 30"])
    days_policy_claim = StringField(required=True, choices=["none", "1 to 7", "8 to 15", "15 to 30", "more than 30"])
    past_number_of_claims = IntField(required=True, min_value=0, max_value=4)
    age_of_policy_holder = IntField(required=True, min_value=17)
    number_of_cars = IntField(required=True, min_value=1, max_value=3)

    def get_normal_fields():
        return [i for i in SinistroModel.__dict__.keys() if i[:1] != '_' and i != "sensitivity_fields" and i not in SinistroModel.sensitivity_fields]
    
    def get_decrypted_field(self, field: str):
        if field not in self.sensitivity_fields:
            raise Exception("Field not mapped")

        return fernet.decrypt(getattr(self, field, None).token).decode()