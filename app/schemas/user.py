from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from ..schemas.perfil  import PerfilUserResponse
from ..schemas.contato import ContatoUserResponse
from ..schemas.credencial import CredencialUserResponse


class UserBase(BaseModel):
    codigo: str
    nome: str
    email: str
    login: str
    area: str
    cargo: str

class UserCreate(UserBase):
    senha: str

class UserResponse(BaseModel):
    id: int
    codigo: str
    nome: str
    criado_em: datetime
    atualizado_em: Optional[datetime] = None
    id_do_responsavel: Optional[int] = None
    ativo: bool
    credencial: CredencialUserResponse
    contato: ContatoUserResponse
    perfil: PerfilUserResponse

    class Config:
        from_attributes = True


class UserCreateResponse(BaseModel):
    mensagem: str
    usuario: UserResponse
