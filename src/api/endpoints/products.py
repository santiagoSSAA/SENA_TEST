from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.utils.db_session import get_db
from src.services import product_service
from src.db import schemas
from src.utils.security import get_current_user, require_role

router = APIRouter()

@router.get("/products", response_model=List[schemas.ProductOut])
def list_products(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return product_service.get_products(db)

@router.get("/products/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return product_service.get_product(db, product_id)

@router.post("/products", response_model=schemas.ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return product_service.create_product(db, product)

@router.put("/products/{product_id}", response_model=schemas.ProductOut)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return product_service.update_product(db, product_id, product)

@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    product_service.delete_product(db, product_id)
    return None
