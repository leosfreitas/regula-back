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
    sensitivity_fields = [
    ]

    user_id = StringField(required=True)
    status = StringField(required=True, choices=["Aberto", "Em análise", "Negado", "Aprovado", "Pago"])
    data = DateTimeField(default=datetime.datetime.now())
    # bo = FileField(required=True)
    cnh = StringField(required=True)
    cpf = StringField(required=True)
    endereco = StringField(required=True)
    data_acidente = DateTimeField(required=True)
    descricao = StringField(required=True)

    def get_normal_fields():
        return [i for i in SinistroModel.__dict__.keys() if i[:1] != '_' and i != "sensitivity_fields" and i not in SinistroModel.sensitivity_fields]
    
    def get_decrypted_field(self, field: str):
        if field not in self.sensitivity_fields:
            raise Exception("Field not mapped")

        return fernet.decrypt(getattr(self, field, None).token).decode()
    
    