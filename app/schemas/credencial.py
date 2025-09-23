from pydantic import BaseModel

class CredencialBase(BaseModel):
    login: str
    senha_hash:str
    salt:str

class CredencialUserCreate(CredencialBase):
    user_id: int

class CredencialUserResponse(CredencialBase):

    class Config:
        from_attributes = True