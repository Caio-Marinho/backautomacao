from sqlalchemy.orm import Session
from ..schemas import UserCreate
from ..repositories import UserRepository
from ..utils import gerar_salt, hash_senha
from sqlalchemy.exc import SQLAlchemyError

class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def criar_usuario(self, user_create: UserCreate):
        try:
            usuario = self.user_repo.criar(user_create)
            self.db.commit()
            self.db.refresh(usuario)
            return usuario
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def listar_usuarios(self):
        return self.user_repo.listar()

    def buscar_usuario_id(self, user_id: int):
        return self.user_repo.buscar_por_id(user_id)

    def deletar_usuario(self, user_id: int):
        return self.user_repo.deletar(user_id)

    def atualizar_usuario(self, user_id: int, user_create: UserCreate):
        usuario = self.user_repo.buscar_por_id(user_id)
        if usuario:
            salt = gerar_salt()
            usuario.senha_hash = hash_senha(user_create.senha, salt)
            usuario.salt = salt
            usuario.codigo = user_create.codigo
            usuario.nome = user_create.nome
            usuario.login = user_create.login
            usuario.email = user_create.email
            self.db.commit()
            self.db.refresh(usuario)
        return usuario

    def verificar_login(self, login: str) -> bool:
        user = self.user_repo.filtrar_por_login(login)
        return user is not None
