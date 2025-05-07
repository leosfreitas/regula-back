import dotenv
from pydantic import BaseModel, FilePath
from typing import Literal
from datetime import datetime
dotenv.load_dotenv()

class Sinistro(BaseModel):
    _id: str
    user_id: str
    status: Literal["Aberto", "Em análise", "Negado", "Aprovado", "Pago"]
    data: datetime
    # bo: FilePath
    cnh: str
    cpf: str
    endereco: str
    data_acidente: datetime
    descricao: str 