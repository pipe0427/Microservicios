from pydantic import BaseModel

class Product(BaseModel):
    name: str
    category : str
    price : int
    stock : int
    bar_code : int