'''接口测试'''

import requests

base_url = 'http://127.0.0.1:8000/api/'

def test_add_event_all_null():
	'测试添加发布会接口'
	datas = {'eid':'', 'limit':'', 'name':'', 'address':'', 'start_time':''}
	r = requests.post(url=base_url+'add_event/', data=datas)
	print(r.url)
	print(r.status_code)
	print(r.json())

def test_add_guest_all_null():
	'测试添加嘉宾接口'
	datas = {'event_id':'', 'realname':'', 'email':'', 'phone':''}
	r = requests.post(url=base_url+'add_guest/', data=datas)
	print(r.url)
	print(r.status_code)
	print(r.json())
	
def test_get_event_list():
	'测试发布会列表接口'
	datas = {'eid':'', 'name':'xiaomi'}
	r = requests.get(url=base_url+'get_event_list/', data=datas)
	print(r.url)
	print(r.status_code)
	print(r.json())

def test_get_guest_list():
	'测试嘉宾列表接口'
	datas = {'eid':'5', 'phone':''}
	r = requests.get(url=base_url+'test_get_guest_list/', data=datas)
	print(r.url)
	print(r.status_code)
	print(r.json())

def test_user_sign():
	'测试发布会签到接口'
	datas = {'eid':'5', 'phone':''}
	r = requests.post(url=base_url+'user_sign/', data=datas)
	print(r.url)
	print(r.status_code)
	print(r.json())

if __name__ == '__main__':
	# test_add_event_all_null()
	# test_add_guest_all_null()
	# test_get_event_list()
	# test_get_guest_list()
	test_user_sign()