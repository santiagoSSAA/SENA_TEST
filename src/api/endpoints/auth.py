from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from src.utils.db_session import get_db
from src.db import schemas, models
from src.utils.security import verify_password, require_role
from src.utils.jwt import create_access_token

router = APIRouter()

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token({"sub": db_user.username, "user_id": db_user.id, "role": getattr(db_user, "role", "user")})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/permissions/{user_id}", response_model=list)
def get_user_permissions(user_id: int, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user.permissions.split(",") if db_user.permissions else []

@router.post("/permissions/{user_id}/add")
def add_permission(user_id: int, permission: str, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    perms = set(db_user.permissions.split(",")) if db_user.permissions else set()
    perms.add(permission)
    db_user.permissions = ",".join(perms)
    db.commit()
    return {"permissions": db_user.permissions.split(",")}

@router.post("/permissions/{user_id}/remove")
def remove_permission(user_id: int, permission: str, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    perms = set(db_user.permissions.split(",")) if db_user.permissions else set()
    perms.discard(permission)
    db_user.permissions = ",".join(perms)
    db.commit()
    return {"permissions": db_user.permissions.split(",")}

@router.post("/signup", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def signup(user: schemas.UserCreate = Body(...), db: Session = Depends(get_db)):
    user.role="admin"
    from src.services import user_service
    return user_service.create_user(db, user)

# Role/permission management endpoints can be expanded as needed.
