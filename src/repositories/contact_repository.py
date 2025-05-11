import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.contact import Contact
from models.contact_model import ContactModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class ContactRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, contact: Contact) -> None: 
        contact_model = ContactModel()
        contact_dict = contact.model_dump()

        for k in ContactModel.get_normal_fields():
            if (k not in contact_dict):
                continue

            contact_model[k] = contact_dict[k]

        for k in ContactModel.sensivity_fields:
            contact_model[k] = SensivityField(fernet=self.fernet, data=contact_dict[k])

        contact_model.status = contact.status
        contact_model.save()

        return None
    
    def get_all_contacts(self) -> list[ContactModel]:
        result = ContactModel.objects()
        contacts = []

        for c in result: 
            contact_dict = c.to_mongo().to_dict()
            contact_dict["_id"] = str(contact_dict["_id"])
            contacts.append(contact_dict)

        return contacts
    
    def delete_contact(self, contact_id: str) -> None:
        contact = ContactModel.objects(id=contact_id).first()
        if not contact:
            return None

        contact.delete()
        return None

    def update_status(self, contact_id: str, status: str) -> ContactModel:
        contact = ContactModel.objects(id=contact_id).first()
        if not contact:
            return None

        contact.status = status
        contact.save()

        return contact