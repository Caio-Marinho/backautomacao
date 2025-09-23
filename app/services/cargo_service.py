from sqlalchemy.orm import Session
from ..repositories import CargoRepository
from ..models import Cargo

class CargoService:
    def __init__(self, db: Session):
        self.db = db
        self.cargo_repo = CargoRepository(db)

    def listar_cargos(self):
        return self.cargo_repo.listar()

    def buscar_por_sigla(self, sigla: str) -> Cargo | None:
        return self.cargo_repo.buscar_por_sigla(sigla)
