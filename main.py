from fastapi import FastAPI

app = FastAPI()


products ={"1":"apple", "2":"iphone" , "3":"samsumng", "4":"saku"}

categories = ["mobile","laptop","pod", "headphones", "gpu", "cpu"]


@app.get('/search')
async def search (q : str):
    return {"search" : q }

@app.get('/items')
async def items(limit : int):
    if limit <= len(categories):
        return {
            "limit" : limit ,
            "categories" : categories[:limit]
                
        }
    
## easy task 
# @app.get('/')
# async def welcome():
#     return {"message":"welcome user"}


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