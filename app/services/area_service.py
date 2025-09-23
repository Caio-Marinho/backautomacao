from sqlalchemy.orm import Session
from ..repositories import AreaRepository
from ..models import Area

class AreaService:
    def __init__(self, db: Session):
        self.db = db
        self.area_repo = AreaRepository(db)

    def listar_areas(self):
        return self.area_repo.listar()

    def buscar_por_sigla(self, sigla: str) -> Area | None:
        return self.area_repo.buscar_por_sigla(sigla)
