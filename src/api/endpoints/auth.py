from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.utils.db_session import get_db
from src.db import schemas, models
from src.utils.security import verify_password, hash_password
from src.utils.jwt import create_access_token

router = APIRouter()

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token({"sub": db_user.username, "user_id": db_user.id, "role": getattr(db_user, "role", "user")})
    return {"access_token": access_token, "token_type": "bearer"}

# Role/permission management endpoints can be expanded as needed.
