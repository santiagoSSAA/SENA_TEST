from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

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
    sales = relationship("Sale", back_populates="user")

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    warehouse = Column(String, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    stock = Column(Integer)
    product = relationship("Product", back_populates="inventory_items")

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    quantity = Column(Integer)
    total = Column(Float)
    product = relationship("Product", back_populates="sales")
    user = relationship("User", back_populates="sales")

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.id"))
    total = Column(Float)

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
