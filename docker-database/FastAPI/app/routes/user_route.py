from fastapi import APIRouter, Body, HTTPException
from models.user import User

from database import UserModel

user_route = APIRouter()


@user_route.get("/")
def get_all_users():
    try:
        users = list(UserModel.select())
        return users
    except Exception as e:
        print(e)
        return {"error": str(e)}


@user_route.get("/{userId}")
def get_user(userId: int):
    try:
        user = UserModel.get(UserModel.id == userId)
        return user
    except Exception as e:
        print(e)
        return {"error": str(e)}


@user_route.post("/users")
def create_user(user: User = Body(...)):
    UserModel.create(username=user.username, email=user.email, password=user.password)
    return user


@user_route.put("/{userId}")
def update_user(userId: int,user: User = Body(...)):
    try:
        existing_user = UserModel.get(UserModel.id == userId)  # Busca el usuario por ID
        
        # Actualiza los campos del usuario con los valores del cuerpo de la solicitud
        existing_user.username = user.username
        existing_user.email = user.email
        existing_user.password = user.password
        
        existing_user.save()  # Guarda los cambios en la base de datos
        return {"message": "User updated successfully"}
    except UserModel.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@user_route.delete("/{userId}")
def delete_user(userId: int):
    try:
        user = UserModel.get(UserModel.id == userId)
        user.delete_instance()
        return "Ususario, borrado"
    except Exception as e:
        print(e)
        return {"error": str(e)}
