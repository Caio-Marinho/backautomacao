from pydantic import BaseModel,Field

class AreaBase(BaseModel):
    sigla_area: str

class AreaUserResponse(AreaBase):

    class Config:
        from_attributes = True
