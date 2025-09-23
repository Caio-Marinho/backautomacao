from sqlalchemy.orm import Session
from ..models import Cargo

class CargoRepository:
    def __init__(self, db: Session):
        self.db = db

    def buscar_por_sigla(self, sigla: str) -> Cargo | None:
        return self.db.query(Cargo).filter(Cargo.sigla_titulo == sigla).first()

    def listar(self) -> list[type[Cargo]]:
        return self.db.query(Cargo).all()
