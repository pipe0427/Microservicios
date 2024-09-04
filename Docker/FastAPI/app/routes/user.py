from fastapi import APIRouter, Body
from schemas.user_schemas import User

user_route = APIRouter()

@user_route.get("/")
def get_all_users():
    try:
        return "All users"
    except Exception as e:
        print(e)
        return {"error": str(e)}

@user_route.get("/{userId}")
def get_user(userId: int):
    try:
        return userId
    except Exception as e:
        print(e)
        return {"error": str(e)}

@user_route.post("/")
def create_user(user: User = Body(...)):
    try:
        return user
    except Exception as e:
        print(e)
        return {"error": str(e)}

@user_route.put("/")
def update_user(user: User = Body(...)):
    try:
        return user
    except Exception as e:
        print(e)
        return {"error": str(e)}

@user_route.delete("/{userId}")
def delete_user(userId: int):
    try:
        return userId
    except Exception as e:
        print(e)
        return {"error": str(e)}
