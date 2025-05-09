from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.db import models

def get_inventory(db: Session):
    return db.query(models.Inventory).all()

def get_inventory_item(db, inventory_id):
    item = db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return item

def create_inventory_item(db, item_data):
    item = models.Inventory(**item_data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update_inventory_item(db, inventory_id, item_data):
    item = db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    for key, value in item_data.dict().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def delete_inventory_item(db, inventory_id):
    item = db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    db.delete(item)
    db.commit()

def get_warehouses(db):
    return list(set([inv.warehouse for inv in db.query(models.Inventory).all()]))

def transfer_inventory(db, warehouse_from, warehouse_to, product_id, quantity):
    from_item = db.query(models.Inventory).filter(models.Inventory.warehouse == warehouse_from, models.Inventory.product_id == product_id).first()
    to_item = db.query(models.Inventory).filter(models.Inventory.warehouse == warehouse_to, models.Inventory.product_id == product_id).first()
    if not from_item or from_item.stock < quantity:
        raise HTTPException(status_code=400, detail="Not enough stock in source warehouse")
    from_item.stock -= quantity
    if to_item:
        to_item.stock += quantity
    else:
        to_item = models.Inventory(warehouse=warehouse_to, product_id=product_id, stock=quantity)
        db.add(to_item)
    db.commit()
    return {"from": warehouse_from, "to": warehouse_to, "product_id": product_id, "quantity": quantity}

def get_inventory_alerts(db: Session):
    alerts = []
    threshold = 10  # Example threshold
    for item in db.query(models.Inventory).all():
        if item.stock <= threshold:
            alerts.append({
                "inventory_id": item.id,
                "product_id": item.product_id,
                "warehouse": item.warehouse,
                "stock": item.stock,
                "alert": "Low stock"
            })
    return alerts
