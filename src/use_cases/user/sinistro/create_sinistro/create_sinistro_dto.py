from pydantic import BaseModel, ConfigDict
from datetime import datetime 

class CreateSinistroDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")

    cnh: str
    endereco: str
    data_acidente: datetime 
    descricao: str
