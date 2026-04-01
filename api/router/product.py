from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from api.schemas import tablecreate



router = APIRouter(prefix="/product")

products={1:"iphone",
         2:"laptop",
         3:"android_phone"}
    
@router.get("/")
async def get_products():
    return {
       "products" : products
    }
    
@router.post("/create")
async def create_product(product :tablecreate):
    if product.id in products :
        raise HTTPException(status_code=400,detail="already exist")
    elif  len(product.name) < 3 :
        raise HTTPException(status_code=400,detail="already exist")
    else :
        products[product.id] =product.name
        return {
            "message" : "product created" ,
            "id" : product.id  ,
            "name" : product.name
        }
    
@router.get("/{id}")
async def retreive(id : int):
    if id not in products :
        raise HTTPException( status_code=404 , detail="product not found")
    else :
        return {
            "id" : id ,
            "product_name " : products[id]
        }
        