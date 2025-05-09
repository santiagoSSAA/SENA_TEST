from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.utils.db_session import get_db
from src.services import inventory_service
from src.db import schemas
from src.utils.security import get_current_user, require_role

router = APIRouter()

@router.get("/inventory", response_model=List[schemas.InventoryOut])
def list_inventory(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return inventory_service.get_inventory(db)

@router.get("/inventory/{inventory_id}", response_model=schemas.InventoryOut)
def get_inventory_item(inventory_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return inventory_service.get_inventory_item(db, inventory_id)

@router.post("/inventory", response_model=schemas.InventoryOut, status_code=status.HTTP_201_CREATED)
def create_inventory_item(item: schemas.InventoryCreate, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return inventory_service.create_inventory_item(db, item)

@router.put("/inventory/{inventory_id}", response_model=schemas.InventoryOut)
def update_inventory_item(inventory_id: int, item: schemas.InventoryCreate, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return inventory_service.update_inventory_item(db, inventory_id, item)

@router.delete("/inventory/{inventory_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inventory_item(inventory_id: int, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    inventory_service.delete_inventory_item(db, inventory_id)
    return None

@router.get("/warehouses", response_model=List[str])
def list_warehouses(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return inventory_service.get_warehouses(db)

@router.post("/warehouses/transfer", response_model=dict)
def transfer_inventory(warehouse_from: str, warehouse_to: str, product_id: int, quantity: int, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return inventory_service.transfer_inventory(db, warehouse_from, warehouse_to, product_id, quantity)

@router.get("/inventory/alerts", response_model=List[dict])
def get_inventory_alerts(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return inventory_service.get_inventory_alerts(db)
