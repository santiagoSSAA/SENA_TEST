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
