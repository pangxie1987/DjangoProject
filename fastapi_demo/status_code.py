from fastapi import FastAPI, Form, UploadFile, File, Body
from starlette.status import HTTP_201_CREATED
from typing import List, Set
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.status import HTTP_201_CREATED
from fastapi.encoders import jsonable_encoder
from datetime import datetime

app = FastAPI()

@app.post("/items/", status_code=HTTP_201_CREATED)	# 使用status_code 声明响应状态码
def create_item(name: str):
	return {"name": name}

@app.post("/login/")
def login(*, 
	username: str=Form(...),
	password: str=Form(...)):
	'''
	接受表单数据
	'''
	return {"username": username}

@app.post("/files/")
def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
def upload_files(file: UploadFile = File(...)):
	'''
	文件上传
	UploadFile文件使用脱机文件
	文件存储在内存中有一个最大限制，如果超过了这个界限，会保存在硬盘中
	'''
	contents = file.file.read()
	return {"filename": file.filename, "contents":contents}

@app.post("/uploadfile/all/")
def upload_files_all(files: List[UploadFile] = File(...)):
	'''
	多个文件上传, 使用List[]
	'''
	return {"filename": [file.filename for file in files]}


@app.post("/files/forms/")
def upload_files_test(
	file: bytes = File(...), fileb: UploadFile=File(...), token: str=Form(...)
	):
	'''
	文件和表单的字段将会被上传为form 数据，你会接收到文件和表单字段
	'''
	return {
		"file_size": len(file),
		"token": token,
		"fileb_content_type": fileb.content_type
	}

class Item(BaseModel):
	name: str
	description: str=None
	price: float
	tax: float=None
	tags: Set[str] = []

@app.get("/items/", 
	response_model=Item,
	tags=["items", "test"], 
	summary="test summary", 
	description="test description",
	response_description="test response_description")
def test_tags(*, item: Item):
	'''
	tag标记，在swagger中分组
	'''
	return item

@app.get("/elements/", tags=["items"], deprecated=True)
def read_elements():
	'''
	deprecated:弃用当前路径
	'''
	return [{"item_id": "foo"}]

@app.get("/items/test33/", include_in_schema=False)
def items_test33():
	'''
	include_in_schema:从API文档中排除这个路径
	'''
	return [{"item_id":"foo"}]

items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}
@app.put("/items/test34/{item_id}")
def items_test34(item_id:str, 
	size: int=Body(None), 
	name: str=Body(None)
	):
	'''
	JSONResponse:设置status_code, 并返回内容
	'''

	if item_id in items:
		item = items[item_id]
		item['name'] = name
		item['size'] = size
	else:
		item = {"name": name, "size": size}
		items[item_id] = item
	return JSONResponse(status_code=HTTP_201_CREATED, content=item)

class Item3(BaseModel):
    title: str
    timestamp: datetime
    description: str = None
fake_db = {}

@app.put("/items/test35/{id}")
def update_item(id:str, item:Item3):
	'''
	jsonable_encoder:接收一个对象，如 Pydantic 模型，并返回JSON兼容版本
	'''
	json_compatible_item_data = jsonable_encoder(item)
	fake_db[id] = json_compatible_item_data
	return fake_db