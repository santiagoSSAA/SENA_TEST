from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.utils.db_session import get_db
from src.services import invoice_service
from src.db import schemas
from src.utils.security import get_current_user, require_role

router = APIRouter()

@router.get("/invoices", response_model=List[schemas.InvoiceOut])
def list_invoices(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return invoice_service.get_invoices(db)

@router.get("/invoices/{invoice_id}", response_model=schemas.InvoiceOut)
def get_invoice(invoice_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return invoice_service.get_invoice(db, invoice_id)

@router.post("/invoices", response_model=schemas.InvoiceOut, status_code=status.HTTP_201_CREATED)
def create_invoice(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    return invoice_service.create_invoice(db, invoice)

@router.delete("/invoices/{invoice_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_invoice(invoice_id: int, db: Session = Depends(get_db), user=Depends(require_role("admin"))):
    invoice_service.delete_invoice(db, invoice_id)
    return None
