from pydantic import BaseModel

class Pc(BaseModel):
    mark : str
    model : str
    processor : str
    ram : int
    storage : int
    