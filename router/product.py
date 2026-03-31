from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/product")
    
@router.get("/")
async def get_products():
    return {
        "product1":"iphone",
        "product2":"laptop"
    }
    
