from fastapi import FastAPI
from router import user
from router import product
app = FastAPI()

app.include_router(user.router)
app.include_router(product.router)