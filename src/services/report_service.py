from sqlalchemy import func
from sqlalchemy.orm import Session
from src.db import models

def get_reports(db: Session, period=None, warehouse=None, product_id=None, user_id=None):
    # Advanced filtering logic
    query = db.query(models.Sale)
    if period:
        # Assume period is 'YYYY-MM' for monthly filtering
        query = query.filter(models.Sale.timestamp.like(f"{period}%"))
    if warehouse:
        query = query.join(models.Product).join(models.Inventory).filter(models.Inventory.warehouse == warehouse)
    if product_id:
        query = query.filter(models.Sale.product_id == product_id)
    if user_id:
        query = query.filter(models.Sale.user_id == user_id)
    sales = query.all()
    # Return a summary for now
    return {"report": [s.id for s in sales], "filters": {"period": period, "warehouse": warehouse, "product_id": product_id, "user_id": user_id}}

def get_analytics(db: Session, group_by=None):
    if group_by == "population":
        # Example: group sales by user role (as a proxy for population)
        result = db.query(models.User.role, func.count(models.Sale.id)).join(models.Sale, models.User.id == models.Sale.user_id).group_by(models.User.role).all()
        return {"analytics": [{"role": r, "sales_count": c} for r, c in result], "group_by": group_by}
    elif group_by == "sector":
        # Example: group sales by warehouse (sector)
        result = db.query(models.Inventory.warehouse, func.count(models.Sale.id)).join(models.Sale, models.Inventory.product_id == models.Sale.product_id).group_by(models.Inventory.warehouse).all()
        return {"analytics": [{"warehouse": w, "sales_count": c} for w, c in result], "group_by": group_by}
    return {"analytics": "Sample analytics", "group_by": group_by}
