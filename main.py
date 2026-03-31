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



# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class studentinput(BaseModel):
#     name: str 
#     marks :int

# class studentoutput(BaseModel):
#     name : str 
#     result : str
    
# @app.post("/student" , response_model= studentoutput)
# async def student(student : studentinput):
#     result = "pass" if student.marks >=40 else "fail"
#     return {
#         "name" : student.name ,
#         "result" : result ,
#         "marks" : student.marks  ### it not print this {👉 FastAPI automatically removes extra field:}
#     }
    
# class OrderInput(BaseModel):
#     product_name: str
#     price: float
#     quantity: int
#     discount: int

# class OrderOutput(BaseModel):
#     product_name: str
#     final_price: float
    
# @app.post("/order", response_model=OrderOutput)
# async def order(order : OrderInput):
#     total_price = order.price * order.quantity
#     final_price = total_price - (total_price * order.discount/ 100)
#     return {
#         "product_name" : order.product_name,
#         "final_price" : final_price
#     }


from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()


@app.post('/product/{id}')
async def product(id:int):
    if id != 1:
        raise HTTPException(status_code=404 , detail= " product is not found")
    return {"product" : "iphone"}
    