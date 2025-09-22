from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.user_service import verificar_login

router = APIRouter(tags=["verificar"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/verificarusers")
def api_verificar_login(data: dict, db: Session = Depends(get_db)):
    login = data.get("login")
    if not login:
        raise HTTPException(status_code=400, detail="Login não fornecido")
    existe = verificar_login(db, login)
    return {"existe": existe}
