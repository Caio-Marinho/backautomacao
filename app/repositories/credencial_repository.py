from sqlalchemy.orm import Session
from ..models import Credencial
from ..utils import hash_senha, gerar_salt


class CredencialRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, user_id: int, login: str, senha: str):
        salt = gerar_salt()
        senha_hash = hash_senha(senha, salt)
        credencial = Credencial(user_id=user_id, login=login, senha_hash=senha_hash, salt=salt)
        self.db.add(credencial)
        self.db.commit()
        self.db.refresh(credencial)
        return credencial

    def buscar_por_user_id(self, user_id):
        self.db.query(Credencial).filter(Credencial.user_id == user_id).first()
