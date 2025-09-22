from pydantic import BaseModel
from ..schemas.cargo import CargoUserResponse
from ..schemas.area import AreaUserResponse


class PerfilUserBase(BaseModel):
    area_id: int
    cargo_id: int

class PerfilUserCreate(PerfilUserBase):
    user_id:int

class PerfilUserResponse(BaseModel):
    area: AreaUserResponse
    cargo: CargoUserResponse

    class Config:
        from_attributes = True
