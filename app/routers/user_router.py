from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..schemas.user import UserCreate, UserResponse, UserCreateResponse
from ..services.user_service import criar_usuario,listar_usuarios,buscar_usuario_id,deletar_usuario,atualizar_usuario,filtrar_por_login


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
    return criar_usuario(db, user)

@router.get(Url_Base, response_model=list[UserResponse])
def listar(db: Session = Depends(get_db)):
    return listar_usuarios(db)

@router.get(Url_Base+"/{user_id}", response_model=UserResponse)
def buscar(user_id: int, db: Session = Depends(get_db)):
    user = buscar_usuario_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

@router.delete(Url_Base+"/{user_id}")
def deletar(user_id: int, db: Session = Depends(get_db)):
    user = deletar_usuario(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"mensagem": f"Usuário {user_id} deletado"}

@router.put(Url_Base+"/{user_id}", response_model=UserResponse)
def atualizar(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    updated_user = atualizar_usuario(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return updated_user

@router.get(Url_Base+"/filter")
def filtrar(login: str, db: Session = Depends(get_db)):
    users = filtrar_por_login(db, login)
    if not users:
        raise HTTPException(status_code=404, detail="Nenhum usuário encontrado")
    return users