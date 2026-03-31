from fastapi import FastAPI
from api.router import user
from api.router import product
app = FastAPI()

app.include_router(user.router)
app.include_router(product.router)