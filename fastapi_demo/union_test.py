'''
测试union.py中的接口
'''
import requests

url = 'http://127.0.0.1:8000'

def test_a1_read_item():
    r = requests.get(url=url+'/items/item2')
    print(r.text)



if __name__ == '__main__':
    test_a1_read_item()