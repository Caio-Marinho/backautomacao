from pydantic import BaseModel,Field

class CargoBase(BaseModel):
    sigla_titulo: str

class CargoUserResponse(CargoBase):


    class Config:
        from_attributes = True
