"""
为接口参加安全机制：认证、签名、AES加密
"""
from django.http import JsonResponse
from sign.models import Event, Guest
from django.contrib import auth as django_auth
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import base64

# 用户认证
def user_auth(request):
	get_http_auth = request.META.get('HTTP_AUTHORIZATION', '')					# 获取用户认证数据
	auth = get_http_auth.split()												# 拆分成list
	try:
		auth_parts = base64.b64decode(auth[1]).decode('utf-8').partition(':')	# 解码并解密，生产('admin', ':', 'admin')这种数据
	except IndexError:
		return 'null'
	username, password = auth_parts[0], auth_parts[2]
	user = django_auth.authenticate(username=username, password=password)		# 使用Django的认证模块对信息进行校验
	if user is not None:
		django_auth.login(request, user)
		return 'success'
	else:
		return 'fail'


# 查询发布会接口---增加用户认证
def get_event_list(request):
	auth_result = user_auth(request)	#调用认证函数
	if auth_result == "null":
		return JsonResponse({'status':10011, 'message':'user auth null'})

	if auth_result == "fail":
		return JsonResponse({'status':10012, 'message':'user auth fail'})

	eid = request.GET.get('eid', '')
	name = request.GET.get('name', '')

	if eid == '' and name == '':
		return JsonResponse({'status':10021, 'message':'parameter error'})
	if eid != '':
		event = {}
		try:
			result = Event.objects.get(id=eid)
		except ObjectDoesNotExist:
			return JsonResponse({'status':10022, 'message':'query result is empty'})
		else:
			event['eid'] = result.id
			event['name'] = result.name
			event['limit'] = result.limit
			event['status'] = result.status
			event['address'] = result.address
			event['start_time'] = result.start_time
			return JsonResponse({'status':200, 'message':'success', 'data':event})
	if name != '':
		datas = []
		results = Event.objects.filter(name_contains=name)
		if results:
			for r in results:
				event = {}
				event['eid'] = result.id
				event['name'] = r.name
				event['limit'] = r.limit
				event['status'] = r.status
				event['address'] = r.address
				event['start_time'] = r.start_time
				datas.append(event)
			return JsonResponse({'status':200, 'message':'success', 'data':datas})
		else:
			return JsonResponse({'status':10022, 'message':'query result is empty'})
