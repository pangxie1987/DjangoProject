import requests
import uuid
import datetime
import time


url = 'http://127.0.0.1:8000'
def test_update_item():
	data={
	'name':'test_update_item',
	'price':12.8
	}

	r = requests.put(url=url+'/items/7', json=data)
	print(r.url)
	print(r.text)

def test_read_item_2():
	data = {
	'skip':1,
	'limit':1
	}
	r = requests.get(url=url+'/items/param/', params=data)
	print(r.url)
	print(r.text)

def test_rea_item_3():
	data = {
	'item_id':'myitemid',
	'q':'test'
	}
	r = requests.get(url=url+'/items/paramteset/test', params=data)
	print(r.url)
	print(r.text)

def test_read_item_test1():
	data = {
	'item_id':'myitemid',
	'q':'test',
	'short':1
	}
	r = requests.get(url=url+'/items/query/test1/test', params=data)
	print(r.url)
	print(r.text)

def test_inser_item():
	data = {
	'name':'insert_item',
	'description':'test',
	'price':19.12
	}
	r = requests.post(url=url+'/items/insert/', json=data)
	print(r.url)
	print(r.text)

def test_inser_item2():
	data = {
	'name':'insert_item',
	'description':'test',
	'price':19.12,
	'tax':5
	}
	r = requests.post(url=url+'/items/insert2/', json=data)
	print(r.url)
	print(r.text)

def test_inser_item3():
	data = {
	'name':'insert_item',
	'description':'test',
	'price':19.12,
	'tax':5
	}
	r = requests.post(url=url+'/items/insert3/12?q=ttt', json=data)
	print(r.url)
	print(r.text)

def read_item_test3():
	data = {
	'name':'insert_item',
	'description':'test',
	'price':19.12,
	'tax':5
	}
	r = requests.get(url=url+'/items/query/test3/', params={'q':'fastapi'})
	print(r.url)
	print(r.text)

def read_item_test4():
	data = {
	'q':'[test123, test456]'	# 传递相同名称的参数，可以用列表q=1&q=2
	}
	r = requests.get(url=url+'/items/query/test4/', params=data)
	print(r.url)
	print(r.text)

def read_item_test5():
	data = {
	'q':'[test123, test456]',	# 传递相同名称的参数，可以用列表q=1&q=2
	'title':'test'
	}
	r = requests.get(url=url+'/items/query/test5/', params=data)
	print(r.url)
	print(r.text)

def read_item_test11():
	data = {
	'q':'test123'
	}
	r = requests.get(url=url+'/item/query/test11/123', params=data)
	print(r.url)
	print(r.text)

def read_item_test12():
	data = {
	'q':'test123'
	}
	r = requests.get(url=url+'/item/query/test12/123', params=data)
	print(r.url)
	print(r.text)

def read_item_test13():
	data = {
		"item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
	    },
	    "user": {
	        "username": "dave",
	        "full_name": "Dave Grohl"
	    }
	}
	r = requests.put(url=url+'/item/query/test13/123', json=data)
	print(r.url)
	print(r.json())

def read_item_test14():
	data = {
		"item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
	    },
	    "user": {
	        "username": "dave",
	        "full_name": "Dave Grohl"
	    },
	    "importance":5
	}
	r = requests.put(url=url+'/item/query/test14/123', json=data)
	print(r.url)
	print(r.json())

def read_item_test15():
	'传入的参数必须是{"item":{}}样式的'
	data = {
		"item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
	    }
	}
	r = requests.put(url=url+'/item/query/test15/123', json=data)
	print(r.url)
	print(r.json())

def read_item_test18():
	'传入的参数必须是{"item":{}}样式的'
	data = {
		"item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2,
        "tags":['test', 'test1', 'test']
	    }
	}
	r = requests.put(url=url+'/item/query/test18/123', json=data)
	print(r.url)
	print(r.json())

def read_item_test19():
	'传入的参数必须是{"item":{}}样式的'
	data = {
		"item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2,
        "tags":['test', 'test1', 'test'],
        'image':{'url':'localhost', 'name':'testimage'}
	    }
	}
	r = requests.put(url=url+'/item/query/test19/123', json=data)
	print(r.url)
	print(r.json())

def read_item_test21():
	'传入的参数必须是{"item":{}}样式的'
	data = {
		"item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2,
        "tags":['test', 'test1', 'test'],
        'image':[{'url':'localhost', 'name':'testimage'},{'url':'localhost22', 'name':'testimage22'}]	# 子模型传递一个列表
	    }
	}
	r = requests.put(url=url+'/item/query/test21/123', json=data)
	print(r.url)
	print(r.json())

def read_item_test22():
	'传入的参数必须是{"item":{}}样式的'
	data = {
		"name":"offer_test",
		"description":"offer_test_desc",
		"price":12.5,

		"item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2,
        "tags":['test', 'test1', 'test'],
        'image':[{'url':'localhost', 'name':'testimage'},{'url':'localhost22', 'name':'testimage22'}]	# 子模型传递一个列表
	    }
	}
	r = requests.post(url=url+'/item/query/test22/', json=data)
	print(r.url)
	print(r.json())

def read_item_test23():
	'传入的参数必须是{"item":{}}样式的'
	data =[{'url':'localhost', 'name':'testimage'},{'url':'localhost22', 'name':'testimage22'}]	# body传递一个列表
	r = requests.post(url=url+'/item/query/test23/', json=data)
	print(r.url)
	print(r.json())

def read_item_test24():
	'时间参数传递'
	data = {
		"start_datetime" :"2020-03-14T03:31:31.182Z",
		"end_datetime":"2020-03-14T03:31:31.182Z",
		"repeat_at":"08:05:32",
		"process_after":5
	}
	r = requests.post(url=url+"/item/query/test24/14bfe806-f1c7-11e6-83b5-0680f3c45093", json=data)
	print(r.url)
	print(r.text)
	# print(r.json())

def test_read_cookies():
	'cookies传参'
	data = {"ads_id":'test'}
	r = requests.get(url=url+'/items/', cookies=data)
	print(r.url)
	print(r.json())

def test_read_heders():
	'headers传参'
	data = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
	r = requests.get(url=url+'/headers/', headers=data)
	print(r.url)
	print(r.json())

def read_headers_test2():
	'headers传参'
	data = {"x-token": "Mozilla/5.0, test999999"}
	r = requests.get(url=url+'/headers/test2/', headers=data)
	print(r.url)
	print(r.json())

def insert_item_test31():
	'响应模型'
	data = {
        "name": "Foo",
        "description": "The pretender",
        "price": 33,
        "tax": 3.2,
        "tags":['test', 'test1', 'test']
	    }
	r = requests.post(url=url+'/items/test31/', json=data)
	print(r.url)
	print(r.json())

def insert_item_test32():
	'输入输出模型'
	data = {
        "username": "zhang",
        "password": "test",
        "email": 'zhang@123.com',
        "full_name": "zhang san"
	    }
	r = requests.post(url=url+'/items/test32/', json=data)
	print(r.url)
	print(r.json())

def user_add():
	'输入输出模型'
	data = {
        "username": "zhang",
        "password": "test",
        "email": 'zhang@123.com',
        "full_name": "zhang san"
	    }
	r = requests.post(url=url+'/user/add/', json=data)
	print(r.url)
	print(r.json())

def read_cars():
	'输入输出模型'
	items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    		},
		} 
	r = requests.get(url=url+'/cars/item2', json=items)	# 传入的item1，影响则为item1形式，item2，响应则为item2
	print(r.url)
	print(r.json())

if __name__ == '__main__':
	read_cars()
	# print(datetime.time)
