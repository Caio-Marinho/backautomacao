from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..schemas.user import UserCreate, UserResponse, UserCreateResponse
from ..services import CentralService
from ..repositories import UserRepository


# -------------------- USERS ROUTER --------------------
router = APIRouter(tags=["users"])
Url_Base = "/users"
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post(Url_Base, response_model=UserCreateResponse)
def criar(user: UserCreate, db: Session = Depends(get_db)):
    cadastrar = CentralService(db)
    return cadastrar.cadastrar_usuario_completo(user)

@router.get(Url_Base, response_model=list[UserResponse])
def listar(db: Session = Depends(get_db)):
    listar = CentralService(db)
    return listar.listar_usuarios_completo()

@router.get(Url_Base+"/{user_id}", response_model=UserResponse)
def buscar(user_id: int, db: Session = Depends(get_db)):
    db = UserRepository(db)
    user = db.buscar_por_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

@router.delete(Url_Base+"/{user_id}")
def deletar(user_id: int, db: Session = Depends(get_db)):
    db = UserRepository(db)
    user = db.deletar(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"mensagem": f"Usuário {user_id} deletado"}

@router.put(Url_Base+"/{user_id}", response_model=UserResponse)
def atualizar(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db = CentralService(db)
    updated_user = db.atualizar_usuario_completo(user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return updated_user

@router.get(Url_Base+"/filter")
def filtrar(login: str, db: Session = Depends(get_db)):
    db = UserRepository(db)
    users = db.filtrar_por_login(login)
    if not users:
        raise HTTPException(status_code=404, detail="Nenhum usuário encontrado")
    return users