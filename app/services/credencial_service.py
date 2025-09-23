from sqlalchemy.orm import Session
from ..repositories import CredencialRepository

class CredencialService:
    def __init__(self, db: Session):
        self.db = db
        self.credencial_repo = CredencialRepository(db)

    def criar_credencial(self, user_id: int, login: str, senha: str):
        return self.credencial_repo.criar(user_id, login, senha)

    def buscar_por_user_id(self, user_id):
        return self.credencial_repo.buscar_por_user_id(user_id)
