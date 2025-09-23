from sqlalchemy.orm import Session
from ..repositories import ContatoRepository

class ContatoService:
    def __init__(self, db: Session):
        self.db = db
        self.contato_repo = ContatoRepository(db)

    def criar_contato(self, user_id: int, email: str):
        return self.contato_repo.criar(user_id, email)

    def buscar_por_user_id(self, user_id):
        return self.contato_repo.buscar_por_user_id(user_id)

