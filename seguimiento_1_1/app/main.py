from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routes.car import car_route
from routes.pc import pc_route
from routes.product import product_route
from routes.book import book_route
from routes.user import user_route

app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

# --------- USER ------------
app.include_router(user_route, prefix = "/users", tags = ["Usuarios"])

# --------- BOOK ------------
app.include_router(book_route, prefix= "/books", tags= ["Books"])

# --------- PRODUCT ------------
app.include_router(product_route, prefix= "/products", tags= ["Products"])

# --------- PC ------------
app.include_router(pc_route, prefix= "/pcs", tags= ["Pcs"])

# --------- CAR ------------
app.include_router(car_route, prefix= "/cars", tags= ["Cars"])


