from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
    registered_on: datetime
