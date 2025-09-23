from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Credencial(Base):
    __tablename__ = "credenciais"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    login = Column(String(50), unique=True, index=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    salt = Column(String(255), nullable=False)

    user = relationship("User", back_populates="credencial")