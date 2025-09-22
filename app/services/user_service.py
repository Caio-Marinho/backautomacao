from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import gerar_salt, hash_senha

def criar_usuario(db: Session, user_create: UserCreate):
    salt = gerar_salt()
    senha_hash = hash_senha(user_create.senha, salt)
    db_user = User(
        codigo=user_create.codigo,
        nome=user_create.nome,
        login=user_create.login,
        email=user_create.email,
        area=user_create.area,
        cargo=user_create.cargo,
        senha_hash=senha_hash,
        salt=salt
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
        "mensagem": "Seu Cadatro fo feito com sucesso\nAguarde algum reponsavel autorizar.",
        "usuario": db_user
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
