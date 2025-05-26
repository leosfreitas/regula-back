import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.sinistro import Sinistro
from models.sinistro_model import SinistroModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class SinistroRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, user_id: str, sinistro: Sinistro) -> SinistroModel:
        sinistro_model = SinistroModel()
        sinistro_dict = sinistro.model_dump()

        for k in SinistroModel.get_normal_fields():
            if (k not in sinistro_dict):
                continue

            sinistro_model[k] = sinistro_dict[k]

        for k in SinistroModel.sensitivity_fields:
            sinistro_model[k] = SensivityField(fernet=self.fernet, data=sinistro_dict[k])

        sinistro_model.user_id = user_id
        sinistro_model.save()

        return sinistro_model
    
    def get_all_sinistros(self) -> list[dict]:
        result = SinistroModel.objects()
        sinistros = []

        for s in result:
            sinistro_dict = s.to_mongo().to_dict()
            sinistro_dict["_id"] = str(sinistro_dict["_id"])  # evitar erro com ObjectId
            sinistros.append(sinistro_dict)

        return sinistros
    
    def get_sinistros_by_user_id(self, user_id: str) -> list[dict]: 
        result = SinistroModel.objects(user_id=user_id)
        sinistros = []

        for s in result:
            sinistro_dict = s.to_mongo().to_dict()
            sinistro_dict["_id"] = str(sinistro_dict["_id"])
            sinistros.append(sinistro_dict)

        return sinistros

    def get_sinistro_by_id(self, sinistro_id: str) -> SinistroModel:
        sinistro = SinistroModel.objects(id=sinistro_id).first()
        if not sinistro:
            return None

        return sinistro
    
    def update_status(self, sinistro_id: str, status: str) -> SinistroModel:
        sinistro = SinistroModel.objects(id=sinistro_id).first()
        if not sinistro:
            return None

        sinistro.status = status
        sinistro.save()

        return sinistro        
    
    def delete_sinistro(self, sinistro_id: str) -> None:
        sinistro = SinistroModel.objects(id=sinistro_id).first()
        if not sinistro:
            return None

        sinistro.delete()
        return None
    