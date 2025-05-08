from pydantic import BaseModel, ConfigDict
from typing import Optional

class CreateContactDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nome: Optional[str] = None
    email: str
    telefone: Optional[str] = None
    empresa: Optional[str] = None
    mensagem: str