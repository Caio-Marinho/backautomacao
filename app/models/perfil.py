from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Perfil(Base):
    __tablename__ = "perfis"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    area_id = Column(Integer, ForeignKey("areas.id"), nullable=False)
    cargo_id = Column(Integer, ForeignKey("cargos.id"), nullable=False)

    area = relationship("Area", back_populates="perfil")
    cargo = relationship("Cargo", back_populates="perfil")
    user = relationship("User", back_populates="perfil")
