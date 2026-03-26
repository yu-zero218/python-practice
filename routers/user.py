from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from services.user import create_user, get_users, update_user, delete_user
from dependencies import get_db

router = APIRouter()

@router.post("/users")
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.name)

@router.get("/users")
def read(db: Session = Depends(get_db)):
    return get_users(db)

@router.put("/users/{user_id}")
def update(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user.name)

@router.delete("/users/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)