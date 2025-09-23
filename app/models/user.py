from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from ..database import Base
from ..utils import dia_hora


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(5), unique=True, index=True, nullable=False)
    nome = Column(String(255), nullable=False)
    criado_em =Column(DateTime,default=dia_hora())
    atualizado_em = Column(DateTime,nullable=True)
    id_do_responsavel = Column(Integer,nullable=True)
    ativo = Column(Boolean,default=False)

    # Relacionamentos
    credencial = relationship("Credencial", uselist=False, back_populates="user")
    contato = relationship("Contato", uselist=False,back_populates="user")
    perfil = relationship("Perfil", uselist=False, back_populates="user")
