import requests


def test_user():
	'user测试'
	base_url = 'http://127.0.0.1:8000/users/'
	auth = ('admin', 'admin')
	r = requests.get(url=base_url+'1/', auth=auth)
	print(r.text)


def test_group():
	'group测试'
	base_url = 'http://127.0.0.1:8000/groups/'
	auth = ('admin', 'admin')
	r = requests.get(url=base_url+'1/', auth=auth)
	print(r.text)


def add_events_data():
	'向event中添加数据'
	datas = {
	'name':'小米1发布会',
	'address':'上海浦东',
	'start_time':'2017-10-11 12:00:00',
	'limit':2000,
	'status':1
	}
	auth = ('admin', 'admin')
	base_url = 'http://127.0.0.1:8000/events/'
	r = requests.post(url=base_url, data=datas, auth=auth)
	print(r.text)

def test_events_get():
	'查询events测试'
	auth = ('admin', 'admin')
	base_url = 'http://127.0.0.1:8000/events/'
	r = requests.get(url=base_url+'1/', auth=auth)
	print(r.text)

if __name__ == '__main__':
	# test_user()
	# test_group()
	# add_events_data()
	test_events_get()