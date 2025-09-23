from fastapi import FastAPI
from .database import Base, engine
from .router import user_router, independente_router
from .models import *

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI MVC + Service + Utils + Hash com Salt")

app.include_router(user_router.router) # pode ser mais de um é sempre chamando o metodo e alimentando ele
app.include_router(independente_router.router)