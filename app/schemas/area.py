from pydantic import BaseModel

class AreaBase(BaseModel):
    sigla_area: str

class AreaUserResponse(AreaBase):
    titulo:str
    class Config:
        from_attributes = True
