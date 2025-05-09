from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.db.database import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    inventory_items = relationship("Inventory", back_populates="product")
    sales = relationship("Sale", back_populates="product")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")  # Added role field
    permissions = Column(String, default="")  # Fine-grained permissions
    sales = relationship("Sale", back_populates="user")

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    warehouse = Column(String, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    stock = Column(Integer)
    expiry_date = Column(DateTime, nullable=True)  # Add expiry_date field
    product = relationship("Product", back_populates="inventory_items")

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    quantity = Column(Integer)
    total = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)  # Add timestamp column
    product = relationship("Product", back_populates="sales")
    user = relationship("User", back_populates="sales")

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.id"))
    total = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

class TransactionHistory(Base):
    __tablename__ = "transaction_history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    action = Column(String)
    entity = Column(String)
    entity_id = Column(Integer)
    details = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
