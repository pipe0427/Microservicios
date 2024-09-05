from fastapi import APIRouter, Body
from schemas.pc_schema import Pc

pc_route = APIRouter()


@pc_route.get("/")
def get_all_pcs():
    try:
        return "All pcs"
    except Exception as e:
        print(e)
        return {"error": str(e)}

@pc_route.get("/{pcId}")
def get_pc(pcId: int):
    try:
        return pcId
    except Exception as e:
        print(e)
        return {"error": str(e)}

@pc_route.post("/")
def create_pc(pc: Pc = Body(...)):
    try:
        return pc
    except Exception as e:
        print(e)
        return {"error": str(e)}

@pc_route.put("/")
def update_pc(pc: Pc = Body(...)):
    try:
        return pc
    except Exception as e:
        print(e)
        return {"error": str(e)}

@pc_route.delete("/{pcId}")
def delete_pc(pcId: int):
    try:
        return pcId
    except Exception as e:
        print(e)
        return {"error": str(e)}