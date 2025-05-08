import dotenv
from pydantic import BaseModel, FilePath
from typing import Literal
from datetime import datetime
dotenv.load_dotenv()

class Contact(BaseModel):
    _id: str
    
    nome: str
    email: str
    telefone: str
    empresa: str
    mensagem: str
    status: Literal["S","N"]