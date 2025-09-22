# app/schemas/user.py
from pydantic import BaseModel

class UserBase(BaseModel):
    codigo: str
    nome: str
    login: str
    email: str
    area: str
    cargo: str

class UserCreate(UserBase):
    senha: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

# Novo schema para retorno de cadastro
class UserCreateResponse(BaseModel):
    mensagem: str
    usuario: UserResponse
