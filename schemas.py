from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    customer_id: int
    product_ids: List[int]

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    status: str

    class Config:
        orm_mode = True
