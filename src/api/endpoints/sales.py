from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.utils.db_session import get_db
from src.services import sales_service
from src.db import schemas
from src.utils.security import get_current_user, require_role

router = APIRouter()

@router.get("/sales", response_model=List[schemas.SaleOut])
def list_sales(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return sales_service.get_sales(db)

@router.get("/sales/{sale_id}", response_model=schemas.SaleOut)
def get_sale(sale_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return sales_service.get_sale(db, sale_id)

@router.post("/sales", response_model=schemas.SaleOut, status_code=status.HTTP_201_CREATED)
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return sales_service.create_sale(db, sale)

@router.put("/sales/{sale_id}", response_model=schemas.SaleOut)
def update_sale(sale_id: int, sale: schemas.SaleCreate, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return sales_service.update_sale(db, sale_id, sale)

@router.delete("/sales/{sale_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sale(sale_id: int, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    sales_service.delete_sale(db, sale_id)
    return None
