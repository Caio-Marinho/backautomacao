from sqlalchemy.orm import Session
from ..repositories import PerfilRepository

class PerfilService:
    def __init__(self, db: Session):
        self.db = db
        self.perfil_repo = PerfilRepository(db)

    def criar_perfil(self, user_id: int, area_id: int, cargo_id: int):
        return self.perfil_repo.criar(user_id, area_id, cargo_id)

    def buscar_por_user_id(self, user_id):
        return self.perfil_repo.buscar_por_user_id(user_id)
