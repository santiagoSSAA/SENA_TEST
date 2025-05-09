from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    role: Optional[str] = "user"  # Added role field

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    product_id: int
    user_id: int
    quantity: int
    total: float

class SaleCreate(SaleBase):
    pass

class SaleOut(SaleBase):
    id: int
    class Config:
        orm_mode = True

class InventoryBase(BaseModel):
    warehouse: str
    product_id: int
    stock: int

class InventoryCreate(InventoryBase):
    pass

class InventoryOut(InventoryBase):
    id: int
    class Config:
        orm_mode = True

class InvoiceBase(BaseModel):
    sale_id: int
    total: float

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceOut(InvoiceBase):
    id: int
    class Config:
        orm_mode = True

class NotificationBase(BaseModel):
    message: str
    user_id: Optional[int] = None

class NotificationCreate(NotificationBase):
    pass

class NotificationOut(NotificationBase):
    id: int
    class Config:
        orm_mode = True
