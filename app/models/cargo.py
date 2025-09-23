from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from ..database import Base

class Cargo(Base):
    __tablename__ = "cargos"

    id = Column(Integer, primary_key=True)
    sigla_titulo = Column(String(10), unique=True, nullable=False)
    titulo = Column(String(50), unique=True, nullable=False)

    perfil = relationship("Perfil", uselist=False, back_populates="cargo")