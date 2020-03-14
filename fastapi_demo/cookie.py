from fastapi import FastAPI, Cookie, Header
from typing import List, Union, Dict
from pydantic import BaseModel


app = FastAPI()

@app.get("/items/")
def read_cookies(*, ads_id: str=Cookie(None)):
	'''
	Cookie是Path和Query的姐妹类，它也同样继承自相同的Param类.
	'''
	return {"ads": ads_id}

@app.get("/headers/")
def read_headers(*, user_agent: str=Header(None)):
	'''
	Header参数
	'''
	return {"User-Agent": user_agent}

@app.get("/headers/test2/")
def read_headers_test2(x_token: List[str]=Header(None)):
	'''
	重复的请求头
	'''
	return {"X_Token Values": x_token}

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: List[str] = []

@app.post("/items/test31/", response_model=Item)
def insert_item_test31(item: Item):
	'''
	响应模型，将输出数据限制为模型的数据.
	'''
	return item

class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: str = None

class UserOut(BaseModel):
    username: str
    email: str
    full_name: str = None

@app.post("/items/test32/", response_model=UserOut)
def insert_item_test32(user: UserIn):
	'''
	UserIn: 输入模型
	UserOut: 输出模型
	'''
	return user


class UserBase(BaseModel):
	username: str
	email: str
	full_name: str=None

class UserIn(UserBase):
	'继承UserBase'
	password: str

class UserOut(UserBase):
	'继承UserBase'
	pass

class UserInDB(UserBase):
	hashed_password: str

def fake_password_hasher(raw_password: str):
	return "supersecret" + raw_password

def fake_save_user(user_in: UserIn):
	hashed_password = fake_password_hasher(user_in.password)
	user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
	print("User saved! ..not really")
	return user_in_db

@app.post("/user/add", response_model=UserOut)
def user_add(*, user_in: UserIn):
	'''
	减少重复代码是 FastAPI 的核心思想之一
	这些模型都共享大量数据，并复制属性名称和类型
	只需要在每个子类中定义出其他的不同的属性即可
	'''
	user_saved = fake_save_user(user_in)
	return user_saved


class BaseItem(BaseModel):
	description: str
	type: str

class CarItem(BaseItem):
	'继承BaseItem'
	type = "car"

class PlaneItem(BaseItem):
	'继承BaseItem'
	type = "plane"
	size: int

items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
} 

@app.get('/cars/{car_id}', response_model=Union[PlaneItem, CarItem])	#将响应声明为两种类型的Union，这意味着响应将是两种类型中的任何一种
def read_cars(car_id: str):
	return items[car_id]


@app.get("/keyword-weights/", response_model=Dict(str, float))
def read_ketword_weights():
	'''
	可以使用简单的任意dict声明响应，仅声明键和值的类型，而无需使用Pydantic模型
	'''
	return {"foo":2.3, "bar":5.5}