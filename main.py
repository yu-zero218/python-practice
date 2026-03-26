from fastapi import FastAPI
from routers import user
from db import engine
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)
