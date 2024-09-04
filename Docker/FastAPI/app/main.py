from fastapi import FastAPI
from starlette.responses import RedirectResponse


#Base de datos
from database import database

app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/docs")