from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.utils.db_session import get_db
from src.services import product_service, user_service, sales_service, inventory_service, report_service, invoice_service, notification_service

router = APIRouter()

@router.get("/products")
def list_products(db: Session = Depends(get_db)):
    return product_service.get_products(db)

@router.post("/products")
def create_product(product: dict, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)

@router.get("/sales")
def list_sales(db: Session = Depends(get_db)):
    return sales_service.get_sales(db)

@router.post("/sales")
def create_sale(sale: dict, db: Session = Depends(get_db)):
    return sales_service.create_sale(db, sale)

@router.get("/users")
def list_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

@router.post("/users")
def create_user(user: dict, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get("/inventory")
def list_inventory(db: Session = Depends(get_db)):
    return inventory_service.get_inventory(db)

@router.get("/reports")
def get_reports(db: Session = Depends(get_db)):
    return report_service.get_reports(db)

@router.get("/invoices")
def list_invoices(db: Session = Depends(get_db)):
    return invoice_service.get_invoices(db)

@router.get("/notifications")
def list_notifications(db: Session = Depends(get_db)):
    return notification_service.get_notifications(db)
