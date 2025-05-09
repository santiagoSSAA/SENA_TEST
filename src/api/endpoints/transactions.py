from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.utils.db_session import get_db
from src.services import transaction_service
from src.db import schemas
from typing import List
from src.utils.security import get_current_user

router = APIRouter()

@router.get("/transactions", response_model=List[schemas.TransactionHistoryOut])
def list_transactions(user_id: int = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return transaction_service.get_transaction_history(db, user_id=user_id)
