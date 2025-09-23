from sqlalchemy.orm import Session
from ..models import Area

class AreaRepository:
    def __init__(self, db: Session):
        self.db = db

    def buscar_por_sigla(self, sigla: str) -> Area | None:
        return self.db.query(Area).filter(Area.sigla_area == sigla).first()

    def listar(self) -> list[Area]:
        return self.db.query(Area).all()
