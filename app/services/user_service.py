from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models import User, Area, Cargo, Contato, Credencial, Perfil
from ..schemas.user import UserCreate
from ..utils.security import gerar_salt, hash_senha

def criar_usuario(db: Session, user_create: UserCreate):
    try:
        salt = gerar_salt()
        senha_hash = hash_senha(user_create.senha, salt)

        # Criar usuário
        db_user = User(codigo=user_create.codigo, nome=user_create.nome)
        db.add(db_user)
        db.flush()  # necessário para pegar db_user.id

        # Consultar IDs de área e cargo existentes
        db_area = db.query(Area).filter(Area.sigla_area == user_create.area).first()
        db_cargo = db.query(Cargo).filter(Cargo.sigla_titulo == user_create.cargo).first()

        if not db_area:
            raise ValueError({"mensagem": f"Área '{user_create.area}' não encontrada."})
        if not db_cargo:
            raise ValueError({"mensagem": f"Cargo '{user_create.cargo}' não encontrado."})

        # Criar contato, credencial e perfil
        db_contato = Contato(user_id=db_user.id, email=user_create.email)
        db_credencial = Credencial(user_id=db_user.id, login=user_create.login, senha_hash=senha_hash, salt=salt)
        db_perfil = Perfil(user_id=db_user.id, area_id=db_area.id, cargo_id=db_cargo.id)

        db.add_all([db_contato, db_credencial, db_perfil])
        db.commit()

        db.refresh(db_user)  # garante que o objeto db_user está atualizado

        return {
            "mensagem": "Cadastro realizado com sucesso\nAguarde a autorização de um supervisor.",
            "usuario": db_user
        }

    except SQLAlchemyError as e:
        db.rollback()
        return {
            "mensagem": "Erro ao criar usuário.",
            "detalhes": str(e)
        }

def listar_usuarios(db: Session):
    return db.query(User).all()


def buscar_usuario_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def deletar_usuario(db: Session, user_id: int):
    user = buscar_usuario_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user


def atualizar_usuario(db: Session, user_id: int, user_data: UserCreate):
    user = buscar_usuario_id(db, user_id)
    if user:
        salt = gerar_salt()
        user.senha_hash = hash_senha(user_data.senha, salt)
        user.salt = salt
        user.codigo = user_data.codigo
        user.nome = user_data.nome
        user.login = user_data.login
        user.email = user_data.email
        user.area = user_data.area
        user.cargo = user_data.cargo
        db.commit()
        db.refresh(user)
    return user


def filtrar_por_login(db: Session, login: str):
    return db.query(User).filter(User.login == login).first()


def verificar_login(db: Session, login: str) -> bool:
    user = filtrar_por_login(db, login)
    return user is not None
