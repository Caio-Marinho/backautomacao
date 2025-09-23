from sqlalchemy.orm import Session
from ..models import Perfil

class PerfilRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, user_id: int, area_id: int, cargo_id: int):
        perfil = Perfil(user_id=user_id, area_id=area_id, cargo_id=cargo_id)
        self.db.add(perfil)
        self.db.commit()
        self.db.refresh(perfil)
        return perfil

    def buscar_por_user_id(self, user_id):
        return self.db.query(Perfil).filter(Perfil.user_id == user_id).first()
