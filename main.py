# from fastapi import FastAPI

# app = FastAPI()


# products ={"1":"apple", "2":"iphone" , "3":"samsumng", "4":"saku"}

# categories = ["mobile","laptop","pod", "headphones", "gpu", "cpu"]
    
   
# # easy task 
# @app.get('/')
# async def welcome():
#     return {"message":"hello world"}


# @app.get('/about/{name}/{age}')
# async def about(name : str , age :int):
#     return {"message" :f"hello my name is {name}",
#             " My age is" : age}


# @app.get('/contact/{contact}')
# async def contact (contact : int):
#     return {"contact" : contact}

# # hard task 
# @app.get('/product/{product_id}')
# async def product( product_id : str):
#     if product_id in products:
#         return {
#             "product_id" :product_id ,
#             "product" : products[product_id]
#         }
#     else :
#         return {"there is no product"}


# @app.get('/search')
# async def search (q : str):
#     return {"search" : q }

# @app.get('/items')
# async def items(limit : int):
#     if limit <= len(categories):
#         return {
#             "limit" : limit ,
#             "categories" : categories[:limit]
                
#         }



from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class input(BaseModel):
    name : str
    password : str
class output(BaseModel):
    name : str 

@app.post("/user" , response_model=output)
async def dev(user : input):
    return user
