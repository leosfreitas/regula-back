import dotenv
from pydantic import BaseModel
from typing import Literal
dotenv.load_dotenv()

class Admin(BaseModel):
    _id: str
    name: str
    email: str
    cpf: str
    phone: str
    password: str

    reset_pwd_token: str = ""
    reset_pwd_token_sent_at: int = 0