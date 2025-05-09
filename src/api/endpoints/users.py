from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.utils.db_session import get_db
from src.services import user_service
from src.db import schemas
from src.utils.security import get_current_user, require_role

router = APIRouter()

@router.get("/users", response_model=List[schemas.UserOut])
def list_users(db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return user_service.get_users(db)

@router.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return user_service.get_user(db, user_id)

@router.post("/users", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db), current_user=Depends(require_role("admin"))):
    return user_service.create_user(db, user)

@router.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db), current_user=Depends(require_role("admin"))):
    return user_service.update_user(db, user_id, user)

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(require_role("admin"))):
    user_service.delete_user(db, user_id)
    return None
