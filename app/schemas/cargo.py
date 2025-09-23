from pydantic import BaseModel

class CargoBase(BaseModel):
    sigla_titulo: str

class CargoUserResponse(CargoBase):


    class Config:
        from_attributes = True
