from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.utils.db_session import get_db
from src.utils.security import get_current_user
from src.db import models, schemas
from typing import List

router = APIRouter()

@router.get("/sync/download", response_model=dict)
def sync_download(db: Session = Depends(get_db), user=Depends(get_current_user)):
    # Download all data for offline use (example: products, sales, inventory, etc.)
    products = db.query(models.Product).all()
    sales = db.query(models.Sale).all()
    inventory = db.query(models.Inventory).all()
    return {
        "products": [schemas.ProductOut.from_orm(p) for p in products],
        "sales": [schemas.SaleOut.from_orm(s) for s in sales],
        "inventory": [schemas.InventoryOut.from_orm(i) for i in inventory]
    }

@router.post("/sync/upload", response_model=dict)
def sync_upload(data: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):
    # Accepts uploaded changes and merges with DB
    updated = []
    for model_name, items in data.items():
        model = getattr(models, model_name.capitalize(), None)
        if not model:
            continue
        for item in items:
            obj = db.query(model).filter_by(id=item.get("id")).first()
            if obj:
                for k, v in item.items():
                    setattr(obj, k, v)
            else:
                db.add(model(**item))
            updated.append(f"{model_name}:{item.get('id')}")
    db.commit()
    return {"status": "merged", "updated": updated}
