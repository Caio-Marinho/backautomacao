from sqlalchemy.orm import Session
from ..models import Contato

class ContatoRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, user_id: int, email: str) -> Contato:
        contato = Contato(user_id=user_id, email=email)
        self.db.add(contato)
        self.db.commit()
        self.db.refresh(contato)
        return contato

    def buscar_por_user_id(self, user_id):
       return self.db.query(Contato).filter(Contato.user_id == user_id).first()
