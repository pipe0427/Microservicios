from fastapi import APIRouter, Body
from models.pc_schema import Pc

from database import PcModel

pc_route = APIRouter()


@pc_route.get("/")
def get_all_pcs():
    try:
        pcs = list(PcModel.select())
        return pcs
    except Exception as e:
        print(e)
        return {"error": str(e)}

@pc_route.get("/{pcId}")
def get_pc(pcId: int):
    try:
        pc = PcModel.get(PcModel.id == pcId)
        return pc
    except Exception as e:
        print(e)
        return {"error": str(e)}

@pc_route.post("/")
def create_pc(pc: Pc = Body(...)):
    try:
        PcModel.create(mark=pc.mark, model=pc.model, processor=pc.ram,ram=pc.ram, storage=pc.storage)
        return pc
    except Exception as e:
        print(e)
        return {"error": str(e)}

@pc_route.put("/")
def update_pc(pcId: int,pc: Pc = Body(...)):
    try:
        existing_pc = PcModel.get(PcModel.id == pcId)

        if existing_pc is None:
            return "The pc doesnt exist"
        else:
            existing_pc.mark = pc.mark
            existing_pc.model = pc.model
            existing_pc.processor = pc.processor
            existing_pc.ram = pc.ram
            existing_pc.storage = pc.storage

            existing_pc.save()
            return "Pc updated successfully"
    except Exception as e:
        print(e)
        return {"error": str(e)}

@pc_route.delete("/{pcId}")
def delete_pc(pcId: int):
    try:
        pc = PcModel.get(PcModel.id == pcId)
        if pc is None:
            return "The pc doesnt exist"
        else: 
            pc.delete_instance()
            return "Pc delete successfully"
    except Exception as e:
        print(e)
        return {"error": str(e)}