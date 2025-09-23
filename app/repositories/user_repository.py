from sqlalchemy.orm import Session
from ..models import User
from ..schemas import UserCreate
from ..utils import gerar_salt, hash_senha

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, user_create: UserCreate) -> User:
        user = User(codigo=user_create.codigo, nome=user_create.nome,)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def listar(self) -> list[User]:
        return self.db.query(User).all()

    def buscar_por_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def deletar(self, user_id: int) -> User | None:
        user = self.buscar_por_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
        return user

    def filtrar_por_login(self, login: str) -> User | None:
        return self.db.query(User).filter(User.login == login).first()
