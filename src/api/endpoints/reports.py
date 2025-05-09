from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.utils.db_session import get_db
from src.services import report_service
from src.utils.security import get_current_user

router = APIRouter()

@router.get("/reports", response_model=dict)
def get_reports(period: str = None, warehouse: str = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return report_service.get_reports(db, period=period, warehouse=warehouse)

@router.get("/analytics", response_model=dict)
def get_analytics(group_by: str = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return report_service.get_analytics(db, group_by=group_by)

@router.get("/reports/export")
def export_reports(format: str = "excel", period: str = None, warehouse: str = None, product_id: int = None, user_id: int = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
    data = report_service.get_reports(db, period=period, warehouse=warehouse, product_id=product_id, user_id=user_id)["report"]
    # For demo, data is a list of sale IDs; in real app, return full dicts
    rows = [{"sale_id": sid} for sid in data]
    if format == "pdf":
        return export_to_pdf(rows, filename="report.pdf")
    return export_to_excel(rows, filename="report.xlsx")

@router.get("/analytics/export")
def export_analytics(format: str = "excel", group_by: str = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
    data = report_service.get_analytics(db, group_by=group_by)["analytics"]
    rows = [{"analytics": data}]
    if format == "pdf":
        return export_to_pdf(rows, filename="analytics.pdf")
    return export_to_excel(rows, filename="analytics.xlsx")
