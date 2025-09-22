from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(5), unique=True, index=True, nullable=False)
    nome = Column(String(255), nullable=False)
    login = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    salt = Column(String(255), nullable=False)
    area = Column(String(5), nullable=False)
    cargo = Column(String(20), nullable=False)
