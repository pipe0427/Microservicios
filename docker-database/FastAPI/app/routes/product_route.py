from fastapi import APIRouter, Body
from models.product_schema import Product

from database import ProducModel

product_route = APIRouter()

@product_route.get("/")
def get_all_products():
    try:
        products = list(ProducModel.select())
        return products
    except Exception as e:
        print(e)
        return {"error": str(e)}

@product_route.get("/{productId}")
def get_product(productId: int):
    try:
        product = ProducModel.get(ProducModel.id == productId)
        return product
    except Exception as e:
        print(e)
        return {"error": str(e)}

@product_route.post("/")
def create_product(product: Product = Body(...)):
    try:
        ProducModel.create(name=product.name, category=product.category, price=product.price, stock=product.stock,bar_code=product.bar_code)
        return product
    except Exception as e:
        print(e)
        return {"error": str(e)}

@product_route.put("/{productId}")
def update_product(productId: int,product: Product = Body(...)):
    try:
        existing_product = ProducModel.get(ProducModel.id == productId)

        if existing_product is None:
            return "The product doesnt exist"
        else:
            existing_product.name = product.name
            existing_product.category = product.category
            existing_product.price = product.price
            existing_product.stock = product.stock
            existing_product.bar_code = product.bar_code

            existing_product.save()
            return "Prodcut updated successfully"
    except Exception as e:
        print(e)
        return {"error": str(e)}

@product_route.delete("/{productId}")
def delete_product(productId: int):
    try:
        product = ProducModel.get(ProducModel.id == productId)
        if product is None:
            return "The product doesnt exist"
        else: 
            product.delete_instance()
            return "Product delete successfully"
    except Exception as e:
        print(e)
        return {"error": str(e)}