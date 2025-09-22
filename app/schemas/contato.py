from pydantic import BaseModel

class ContatoBase(BaseModel):
    email: str

class ContatoUserCreate(ContatoBase):
    user_id: int

class ContatoUserResponse(BaseModel):
    email: str

    class Config:
        from_attributes = True
