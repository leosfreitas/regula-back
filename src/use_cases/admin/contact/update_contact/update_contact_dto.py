from pydantic import BaseModel, ConfigDict
from typing import Literal

class UpdateContactDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    status: Literal["S", "N"]