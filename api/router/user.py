from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/users")

class user(BaseModel):
    user : str
    age : int 
    income : int
    
@router.get('/')
async def get_users():
    return {
        "user1" : "shivam" ,
        "user2" : "saksham"
    }
    
@router.post("/user_create")
async def create_user(create : user):
    return {
        "user" : create.user ,               # there is two method for post one is query parameter 
        "age" : create.age ,
        "income" : create.income    
    }
    
@router.post("/user_create/{user}/{age}/{income}")
async def create_user(user :str , age : int , income :float):
    return {
        "user" : user ,                      # there is two method for post one is path parameter 
        "age" : age ,
        "income" : income    
    }