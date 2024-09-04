from pydantic import BaseModel

class Car(BaseModel):
    mark: str
    model: str
    age: int
    color: str
    price: int