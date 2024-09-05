from fastapi import APIRouter, Body
from schemas.car_schema import Car

car_route = APIRouter()

@car_route.get("/")
def get_all_cars():
    try:
        return "All cars"
    except Exception as e:
        print(e)
        return {"error": str(e)}

@car_route.get("/{carId}")
def get_car(carId: int):
    try:
        return carId
    except Exception as e:
        print(e)
        return {"error": str(e)}

@car_route.post("/")
def create_car(car: Car = Body(...)):
    try:
        return car
    except Exception as e:
        print(e)
        return {"error": str(e)}

@car_route.put("/")
def update_car(car: Car = Body(...)):
    try:
        return car
    except Exception as e:
        print(e)
        return {"error": str(e)}

@car_route.delete("/{carId}")
def delete_car(carId: int):
    try:
        return carId
    except Exception as e:
        print(e)
        return {"error": str(e)}
