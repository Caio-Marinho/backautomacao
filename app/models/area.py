from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from app.database import Base

class Area(Base):
    __tablename__ = "areas"

    id = Column(Integer, primary_key=True)
    sigla_area = Column(String(10), unique=True, nullable=False)
    titulo = Column(String(50), unique=True, nullable=False)

    perfil = relationship("Perfil", uselist=False, back_populates="area")