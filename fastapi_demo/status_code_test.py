import requests
import os
from datetime import datetime

url = 'http://127.0.0.1:8000'

def test_create_item():
	'测试响应状态码'

	r = requests.post(url=url+'/items/', params={"name": "test"})
	print(r.url)
	print(r.json())
	print(r.status_code)

def test_login():
	'表单数据, 用data传递'

	r = requests.post(url=url+'/login/', data={"username": "test", "password":"123456"})
	print(r.url)
	print(r.json())
	print(r.status_code)

def test_upload_files():
	'文件上传'
	files1 = os.path.join(os.path.dirname(__file__), 'files', "testfile1.docx")
	print(files1)
	data = {"file":('testfile1.docx', open(files1, 'rb'), 'text/plain')}
	headers = {"Content-Type": "multipart/form-data"}
	r = requests.post(url=url+'/uploadfile/', files=data, headers=headers)
	print(r.url)
	print(r.text)
	# print(r.json())
	print(r.status_code)

def test_upload_files_test():
	'表单数据, 用data传递'
	files1 = os.path.join(os.path.dirname(__file__), 'files', "testfile1.docx")
	files2 = os.path.join(os.path.dirname(__file__), 'files', "testfile2.txt")
	files1_bytes = open(files1, 'rb')
	files2_bytes = open(files2, 'rb')
	data = {"token":"123", "file":files1_bytes, "fileb":files2_bytes}
	r = requests.post(url=url+'/files/forms/', files=data)
	print(r.url)
	print(r.json())
	print(r.status_code)

def test_items_test34():
	'测试响应状态码'
	data = {"name": "Fighters", "size": 6}

	r = requests.put(url=url+'/items/test34/foo123', json=data)
	print(r.url)
	print(r.json())
	print(r.status_code)

def test_update_item():
	'jsonable_encoder'
	data = {
		"title": "Fighters", 
		"timestamp":str(datetime.now()),
		"description": "test jsonable_encoderjsonable_encoder"}

	r = requests.put(url=url+'/items/test35/foo123', json=data)
	print(r.url)
	print(r.json())
	print(r.status_code)

if __name__ == '__main__':
	test_update_item()
	# filepath = os.path.join(os.path.dirname(__file__), 'files')
	# print(filepath)