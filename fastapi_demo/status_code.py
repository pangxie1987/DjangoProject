from fastapi import FastAPI, Form, UploadFile, File
from starlette.status import HTTP_201_CREATED
from typing import List

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