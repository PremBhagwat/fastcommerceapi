from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import crud
import schemas
import config_db




app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = config_db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Product Routes

# Create a product
@app.post("/products/", response_model=schemas.Product)

async def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(name=product.name, description=product.description, price=product.price)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
    

# # Get a specific product by ID
# @app.get("/products/{product_id}", response_model=schemas.Product)
# def get_product(product_id: int, db: Session = Depends(get_db)):
#     db_product = crud.get_product(db=db, product_id=product_id)
#     if not db_product:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return db_product

# # Update a product's name and description
# @app.put("/products/{product_id}", response_model=schemas.Product)
# def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
#     db_product = crud.update_product(db=db, product_id=product_id, product=product)
#     if not db_product:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return db_product

# # Delete a product by ID
# @app.delete("/products/{product_id}")
# def delete_product(product_id: int, db: Session = Depends(get_db)):
#     db_product = crud.delete_product(db=db, product_id=product_id)
#     if not db_product:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return {"message": "Product deleted successfully"}

# # Order Routes

# # Create a new order
# @app.post("/orders/", response_model=schemas.Order)
# def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
#     db_order = crud.create_order(db=db, order=order)
#     if not db_order:
#         raise HTTPException(status_code=400, detail="Failed to create order")
#     return db_order

# # Update an order's status (e.g., from "pending" to "shipped")
# @app.put("/orders/{order_id}", response_model=schemas.Order)
# def update_order_status(order_id: int, status: str, db: Session = Depends(get_db)):
#     db_order = crud.update_order_status(db=db, order_id=order_id, status=status)
#     if not db_order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return db_order

# # Delete an order by ID
# @app.delete("/orders/{order_id}")
# def delete_order(order_id: int, db: Session = Depends(get_db)):
#     db_order = crud.delete_order(db=db, order_id=order_id)
#     if not db_order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return {"message": "Order deleted successfully"}
