from fastapi import APIRouter, Body
from schemas.product_schema import Product

product_route = APIRouter()

@product_route.get("/")
def get_all_products():
    try:
        return "All products"
    except Exception as e:
        print(e)
        return {"error": str(e)}

@product_route.get("/{productId}")
def get_product(productId: int):
    try:
        return productId
    except Exception as e:
        print(e)
        return {"error": str(e)}

@product_route.post("/")
def create_product(product: Product = Body(...)):
    try:
        return product
    except Exception as e:
        print(e)
        return {"error": str(e)}

@product_route.put("/")
def update_product(product: Product = Body(...)):
    try:
        return product
    except Exception as e:
        print(e)
        return {"error": str(e)}

@product_route.delete("/{productId}")
def delete_product(productId: int):
    try:
        return productId
    except Exception as e:
        print(e)
        return {"error": str(e)}