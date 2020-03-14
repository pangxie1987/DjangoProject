from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Schema
from enum import Enum
from typing import Optional, List

app = FastAPI()

class Item(BaseModel):
	name:str
	price:float
	is_offer:bool = None

class ModelName(str, Enum):
	alexnet = "alexnet"
	resnet = "resnet"
	lenet = "lenet"

@app.get("/")
def read_root():
	return {"hello":"world"}

@app.get("/items/{item_id}")
def read_item(item_id:int, q:str=None):
	return {"item_id": item_id, "q":q}

@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
	return {"item_name":item.name,  "item_id":item_id}


@app.get('/user/me')
def read_user_me():
	return {'user':'the cureent user'}

@app.get('/user/{user_id}')
def read_user(user_id:str):
	return {'user_id':user_id}

@app.get("/model/{model_name}")
def get_model(model_name: ModelName):
	"枚举类"
	if model_name == ModelName.alexnet:
		return {"model_name":model_name, "message":"Deep Learing FTW"}
	if model_name.value == "lenet":
		return {"model_name":model_name, "message":"LeCNN all the images"}
	return {'model_name':model_name, "message":"Have some residuals"}

@app.get("/files/{file_path:path}")
def read_file_path(file_path: str):
	"获取文件路径"
	return {"file_path": file_path}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/param/")
def read_item_2(skip: int=0, limit: int=10):
	"Query参数"
	return fake_items_db[skip: skip+limit]

@app.get("/items/paramteset/{item_id}")
def read_item_3(item_id: str, q:str = None):
	if q:
		return {"item_id":item_id, "q":q}
	return {"item_id": item_id}

@app.get("/items/query/test1/{item_id}")
def read_item_test1(item_id: str, q: str=None, short: bool=False):
	item = {"item_id": item_id}
	if q:
		item.update({"q":q})
	if not short:
		item.update({"descption": "This is an amazing item that has a long descption"})
	return item

@app.get("/items/query/test2/{item_id}")
def read_item_test1(item_id: str, limit: Optional[int] = None):
	"你可以使用 Optional 告诉 mypy，这个值可能是 None"
	item = {"item_id": item_id}
	return item

class Item2(BaseModel):
	name:str
	description: str = None
	price:float
	tax:float = None

@app.post('/items/insert/')
def inser_item(item: Item2):
	return item

@app.post('/items/insert2/')
def inser_item2(item: Item2):
	item_dict = item.dict()
	if item.tax:
		pirce_with_tax = item.price+item.tax
		item_dict.update({'pirce_with_tax':pirce_with_tax})
	return item_dict

@app.post('/items/insert3/{item_id}')
def inser_item3(item_id:int, item: Item2, q:str=None):
	result = {"item_id":item_id, **item.dict()}
	if q:
		result.update({"q":q})
	return result

@app.get("/items/query/test3/")
def read_item_test3(
	q: str = Query(None, min_length=2, max_length=50, regex='^fastapi$')):
	'''
	现在使用 Query方法设置参数的默认值，另外设置 max_length 为 50
	max_length  最大长度
	min_length	最小长度
	regex		正则表达式
	'''
	results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
	if q:
		results.update({'q':q})
	return results

@app.get("/items/query/test4/")
def read_item_test4(q: List[str] = Query(None)):
	'''
	设置Query 参数 列表 / 多个值
	'''
	results = {"q": q}
	return results

@app.get("/items/query/test5/")
def read_item_test5(
	q: str = Query(None, 
		title="Query string", 
		min_length=3,
		description="Query string for the items"
		)):
	'''
	声明多元数据
	'''
	results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
	if q:
		results.update({'q':q})
	return results

@app.get("/items/query/test6/")
def read_item_test6(
	q: str = Query(None, 
		alias="item-query" 
		)):
	'''
	别名参数alias
	'''
	results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
	if q:
		results.update({'q':q})
	return results


@app.get("/items/query/test7/")
def read_item_test7(
	q: str = Query(None, 
		title="Query string", 
		min_length=3,
		description="Query string for the items",
		deprecated=True
		)):
	'''
	显示弃用参数 deprecated
	'''
	results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
	if q:
		results.update({'q':q})
	return results

@app.get("/item/query/test8/{item_id}")
def read_item_test8(
	q: str=Query(None, title="Query string for the items"),
	item_id: int=Path(..., title="The ID of the item to get")):
	'''
	Path:路径参数
	...：标识必填参数
	'''
	results = {"item_id": item_id}
	if q:
		results.update({"q":q})
	return results


@app.get("/item/query/test9/{item_id}")
def read_item_test9(
	*,
	item_id: int=Path(..., title="The ID of the item to get"),
	q: str):
	'''
	传递*作为函数的第一个参数。
	*之后所有参数都应称为关键字参数
	'''
	results = {"item_id": item_id}
	if q:
		results.update({"q":q})
	return results

@app.get("/item/query/test11/{item_id}")
def read_item_test11(
	*,
	item_id: int=Path(..., title="The ID of the item to get", ge=1),
	q: str):
	'''
	数字验证：大于或等于->给前端使用（H5，WEB等）
	当ge = 1时，item_id必须是整数
	'''
	results = {"item_id": item_id}
	if q:
		results.update({"q":q})
	return results

@app.get("/item/query/test12/{item_id}")
def read_item_test12(
	*,
	item_id: int=Path(..., title="The ID of the item to get", gt=0, le=10),
	q: str):
	'''
	数字验证器->给前端使用（H5，WEB等）
	gt:大于
	le:小于等于
	'''
	results = {"item_id": item_id}
	if q:
		results.update({"q":q})
	return results


class Goods(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class User(BaseModel):
	username: str
	full_name: str=None

@app.put("/item/query/test13/{item_id}")
def read_item_test13(*, item_id:int, item:Goods, user:User):
	'''
	定义多个body参数
	'''
	results = {"item_id":item_id, "item":item, "user":user}
	return results


@app.put("/item/query/test14/{item_id}")
def read_item_test14(*, item_id:int, item:Goods, user:User, importance:int=Body(...)):
	'''
	使用Body参数，让FastAPI将其视为请求体的key：
	'''
	results = {"item_id":item_id, "item":item, "user":user, "importance":importance}
	return results

@app.put("/item/query/test15/{item_id}")
def read_item_test15(*, item_id:int, item:Item=Body(..., embed=True)):
	'''
	得到一个带有key的JSON，并且在key对应的包含模型内容
	'''
	results = {"item_id":item_id, "item":item}
	return results

class Goods2(BaseModel):
    name: str
    description: str = Schema(None, title="The description of the item", max_length=100)
    price: float=Schema(..., gt=0, description="The price must be greater than zero")
    tax: float = None

@app.put("/item/query/test16/{item_id}")
def read_item_test16(*, item_id:int, item:Goods2=Body(..., embed=True)):
	'''
	将Schema与模型属性一起使用
	'''
	results = {"item_id":item_id, "item":item}
	return results


@app.put("/item/query/test17/{item_id}")
def read_item_test17(*, item_id:int, item:Goods2=Body(
	...,
	example={"name":"foo", "description":'A very nice Item', "price":12.5, "tax":3.4})
	):
	'''
	将JSON模式示例字段传递给 body请求 JSON模式 
	'''
	results = {"item_id":item_id, "item":item}
	return results