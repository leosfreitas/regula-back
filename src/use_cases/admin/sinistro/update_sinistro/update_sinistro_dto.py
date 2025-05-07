from pydantic import BaseModel, ConfigDict
from typing import Literal

class UpdateSinistroDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    status: Literal["Aberto", "Em análise", "Negado", "Aprovado", "Pago"]