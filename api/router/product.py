from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from api.schemas import tablecreate
from fastapi import Depends
from api.Database import SessionLocal
from api.table import Product



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
        

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add_product")
async def create_product(name: str, db=Depends(get_db)):
    new_product = Product(name=name)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return new_product

@router.get("/db/all")
async def get_products(db=Depends(get_db)):
    return db.query(Product).all()

@router.get("/get_product/{id}")
async def get_product(id: int, db=Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="Not found")
    
    return product