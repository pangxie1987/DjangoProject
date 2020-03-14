import requests

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

if __name__ == '__main__':
	read_item_test15()