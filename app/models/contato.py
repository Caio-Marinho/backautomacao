from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Contato(Base):
    __tablename__ = "contatos"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    email = Column(String(50), unique=True, nullable=False)

    user = relationship("User", back_populates="contato")