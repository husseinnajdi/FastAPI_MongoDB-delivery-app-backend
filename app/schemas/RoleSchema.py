from pydantic import BaseModel
from datetime import datetime

class RoleCreate(BaseModel):
    id: int
    name: str
    description: str