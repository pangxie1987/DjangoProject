'''接口测试'''
from time import time
import requests, hashlib
from Crypto.Cipher import AES
import json
import base64

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

def test_sec_get_event_list():
	'测试发布会列表接口-用户认证'
	auth_user = ('admin', 'admin')
	datas = {'eid':7}
	r = requests.get(url='http://127.0.0.1:8000/api/sec_get_event_list/', auth=auth_user, params=datas)
	print(r.url)
	print(r.status_code)
	print(r.json())


def test_add_event_success_sign():
	"新增发布会：时间戳+签名"

	# 客户端时间戳及签名
	api_key = "#Guest-Bugmaster"
	now_time = time()
	client_time = str(now_time).split('.')[0]
	# sign
	md5 = hashlib.md5()
	sign_str = client_time + api_key
	sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
	md5.update(sign_bytes_utf8)
	sign_md5 = md5.hexdigest()

	url = 'http://127.0.0.1:8000/api/sec_add_event/'
	# 请求数据
	payload = {'eid':11,'name':'小米11-pro发布会11','limit':'23000','address':'上海梅赛德斯奔驰中心','start_time':'2017-01-01 19:00:00','time':client_time,'sign':sign_md5}
	r = requests.post(url=url, data=payload)
	print(r.text)

def encryptBase64(src):
	return base64.urlsafe_b64encode(src)

def encryptAES(src, key):
	'生成AES密文'
	
	iv = "1172311105789011"
	BS = 16
	pad= lambda s:s + (BS-len(s)%BS) * chr(BS-len(s)%BS)
	# bs = AES.block_size
	# pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
	cryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
	ciphertext = cryptor.encrypt(pad(src.encode('utf-8')))
	return encryptBase64(ciphertext)

def test_aes_interface():
	"AES 加密"
	
	base_url = "http://127.0.0.1:8000/api/sec_get_guest_list"
	app_key = 'W7v4D60fds2Cmk2U'

	payload = {'eid':'5', 'phone':'13455555555'}
	encoded = encryptAES(json.dumps(payload), app_key).decode()
	r = requests.post(base_url, data={'data': encodeed})
	print(r.text)




if __name__ == '__main__':
	# test_add_event_all_null()
	# test_add_guest_all_null()
	# test_get_event_list()
	# test_get_guest_list()
	# test_user_sign()
	# test_sec_get_event_list()
	# test_add_event_success_sign()
	test_aes_interface()
