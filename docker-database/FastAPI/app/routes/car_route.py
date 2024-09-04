from fastapi import APIRouter, Body
from models.car_schema import Car

from database import CarModel

car_route = APIRouter()

@car_route.get("/")
def get_all_cars():
    try:
        car = list(CarModel.select())
        return car
    except Exception as e:
        print(e)
        return {"error": str(e)}

@car_route.get("/{carId}")
def get_car(carId: int):
    try:
        car = CarModel.get(CarModel.id == carId)
        return car
    except Exception as e:
        print(e)
        return {"error": str(e)}

@car_route.post("/")
def create_car(car: Car = Body(...)):
    try:
        CarModel.create(mark=car.mark, model=car.model, age=car.age,color=car.color, price=car.price)
        return car
    except Exception as e:
        print(e)
        return {"error": str(e)}

@car_route.put("/")
def update_car(carId: int,car: Car = Body(...)):
    try:
        existing_car = CarModel.get(CarModel.id == carId)

        if existing_car is None:
            return "The car doesnt exist"
        else:
            existing_car.mark = car.mark
            existing_car.model = car.model
            existing_car.age = car.age
            existing_car.color = car.color
            existing_car.price = car.price

            existing_car.save()
            return "Car updated successfully"
    except Exception as e:
        print(e)
        return {"error": str(e)}

@car_route.delete("/{carId}")
def delete_car(carId: int):
    try:
        car = CarModel.get(CarModel.id == carId)
        if car is None:
            return "The car doesnt exist"
        else: 
            car.delete_instance()
            return "Car delete successfully"
    except Exception as e:
        print(e)
        return {"error": str(e)}
