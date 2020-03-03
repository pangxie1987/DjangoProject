# -*-coding:utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime


# Create your views here.
# 首页
def index(request):
	return render(request, "index.html")

# 登陆动作
def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)	# 登陆
			request.session['user'] = username	# 将session信息记录到浏览器中
			response = HttpResponseRedirect('/event_manage/')
			return response

		else:
			return render(request, 'index.html', {'error':'username or password error!'})

# 发布会管理
@login_required
def event_manage(request):
	# username = request.COOKIES.get('user', '')	# 读取浏览器cookie
	event_list = Event.objects.all()
	username = request.session.get('user', '')	# 读取浏览器session
	return render(request, 'event_manage.html', {'user':username, 'events':event_list})

# 发布会名称搜索
@login_required
def search_name(request):
	username = request.session.get("user", "")
	search_name = request.GET.get("name", "")
	#search_name_bytes = search_name.encode(encoding="utf-8")
	event_list = Event.objects.filter(name__contains=search_name)
	return render(request, "event_manage.html", {"user":username, "events":event_list})


# 嘉宾管理
@login_required
def guest_manage(request):
	username = request.session.get('user', '')
	guest_list = Guest.objects.all()
	paginator = Paginator(guest_list, 5)	# 分页，每页5条
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		#如果page不是整数，取第一页面数据
		contacts = paginator.page(1)
	except EmptyPage:
		#如果page不在范围内，取最后一页面
		contacts = paginator.page(paginator.num_pages)
	return render(request, "guest_manage.html", {'user': username, 'guests':contacts})

# 嘉宾姓名搜索
@login_required
def search_name_guest(request):
	username = request.session.get("user", "")
	search_name = request.GET.get("realname", "")
	#search_name_bytes = search_name.encode(encoding="utf-8")
	guest_list = Guest.objects.filter(realname__contains=search_name)
	paginator = Paginator(guest_list, 5)	# 分页，每页5条
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		#如果page不是整数，取第一页面数据
		contacts = paginator.page(1)
	except EmptyPage:
		#如果page不在范围内，取最后一页面
		contacts = paginator.page(paginator.num_pages)
	return render(request, "guest_manage.html", {"user": username, "guests":contacts})


# 签到页面
@login_required
def sign_index(request, eid):
	event = get_object_or_404(Event, id=eid)
	# sign_count = Guest.objects.filter(event_id=eid, sign='1').count()	#已签到人数
	sign_yes = sign_count(eid)
	return render(request, 'sign_index.html', {'event': event, 'sign_count': sign_yes})

# 签到动作
@login_required
def sign_index_action(request, eid):
	event = get_object_or_404(Event, id=eid)
	phone = request.POST.get('phone', '')
	print(phone)
	result = Guest.objects.filter(phone=phone)
	if not result:
		return render(request, 'sign_index.html', {'event': event, 'hint':'phone error.'})

	result = Guest.objects.filter(phone=phone, event_id=eid)
	if not result:
		return render(request, 'sign_index.html', {'event': event, 'hint':'event_id or phone error.'})

	result = Guest.objects.get(phone=phone, event_id=eid)
	if result.sign:
		return render(request, 'sign_index.html', {'event': event, 'hint':'user has sign in.'})
	else:
		Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
		sign_yes = sign_count(eid)
		return render(request, 'sign_index.html', {'event': event, 'hint': 'sign in success', 'guest': result, 'sign_count': sign_yes})

# 统计发布会下已签到人数
def sign_count(eid):
	sign_num = Guest.objects.filter(event_id=eid, sign='1').count()	#已签到人数
	all_guest = Guest.objects.filter(event_id=eid).count()	#此发布会下所有的人数
	no_sign = all_guest-sign_num
	if no_sign == 0:
		sign_all = '已全部签到'
	else:
		sign_all = '总人数：%s，未签到人数：%s'%(all_guest, no_sign)
	return sign_all

# 退出动作
@login_required
def logout(request):
	auth.logout(request)	#退出登录
	response = HttpResponseRedirect('/index/')
	return response

# 添加嘉宾页面（发布会管理入口）
@login_required
def event_insert_guest_index(request, eid):
	event = get_object_or_404(Event, id=eid)
	return render(request, 'event_insert_guest_index.html', {'event': event})

# 添加嘉宾动作（发布会管理入口）
@login_required
def event_insert_guest_action(request, eid):
	event = get_object_or_404(Event, id=eid)
	phone = request.POST.get('phone', '')
	realname = request.POST.get('realname', '')
	email = request.POST.get('email', '')
	sign = '0'
	create_time = datetime.now()
	print(eid, phone, realname, email, sign, create_time)
	try:
		new_guest = Guest.objects.create(event_id=eid, phone=phone, realname=realname, email=email, sign=sign, create_time=create_time)
	except:
		new_guest={}
	if new_guest:

		return render(request, 'event_insert_guest_index.html', {'event':event, 'guest': new_guest, 'hint':'嘉宾添加成功'})
	else:
		return render(request, 'event_insert_guest_index.html', {'event':event, 'guest': new_guest, 'hint':'添加失败了'})

# 新增发布会页面
@login_required
def event_insert_index(request):
	# event = get_object_or_404(Event, id=eid)
	return render(request, 'event_insert_index.html')

# 新增发布会动作
@login_required
def event_insert_action(request):
	name = request.POST.get('name', '')
	limit = request.POST.get('limit', '')
	address = request.POST.get('address', '')
	start_time = request.POST.get('start_time', '')
	create_time = datetime.now()
	status = '0'
	try:
		new_event = Event.objects.create(name=name, limit=limit, address=address, status=status, start_time=start_time, create_time=create_time)
	except:
		new_event={}
	if new_event:

		return render(request, 'event_insert_index.html', {'event': new_event, 'hint':'发布会新增成功'})
	else:
		return render(request, 'event_insert_index.html', {'event': new_event, 'hint':'发布会新增失败了'})

# 修改发布会页面
@login_required
def event_update_index(request, eid):
	event = get_object_or_404(Event, id=eid)
	return render(request, 'event_update_index.html', {'event':event})

# 修改发布会动作
@login_required
def event_update_action(request, eid):
	name = request.POST.get('name', '')
	limit = request.POST.get('limit', '')
	address = request.POST.get('address', '')
	# start_time = request.POST.get('start_time', '')
	# create_time = datetime.now()
	status = request.POST.get('status', '')
	update_flag = Event.objects.filter(id=eid).update(name=name, limit=limit, address=address, status=status)	#修改成功后update_flag=1,否则=0
	new_event = Event.objects.get(id=eid)
	if new_event:
		return render(request, 'event_update_index.html', {'new_event': new_event, 'hint':'发布会修改成功'})
	else:
		return render(request, 'event_update_index.html', {'new_event': new_event, 'hint':'发布会修改失败了'})

# 删除发布会
@login_required
def event_delete(request, eid):
	event = Event.objects.filter(id=eid)
	if not event:
		messages.error(request, '数据不存在')
		response = HttpResponseRedirect('/guest_manage/')
		return response
	else:
		event.delete()
		response = HttpResponseRedirect('/event_manage/')
		return response

# 修改嘉宾页面
@login_required
def guest_update_index(request, eid):
	guest = get_object_or_404(Guest, id=eid)
	return render(request, 'guest_update_index.html', {'guest':guest})

# 修改嘉宾动作
@login_required
def guest_update_action(request, eid):
	phone = request.POST.get('phone', '')
	email = request.POST.get('email', '')
	sign = request.POST.get('sign', '')

	update_flag = Guest.objects.filter(id=eid).update(phone=phone, email=email, sign=sign)	#修改成功后update_flag=1,否则=0
	new_guest = Guest.objects.get(id=eid)
	if update_flag:
		return render(request, 'guest_update_index.html', {'new_guest': new_guest, 'hint':'嘉宾修改成功'})
	else:
		return render(request, 'guest_update_index.html', {'new_guest': new_guest, 'hint':'嘉宾修改失败了'})

# 删除嘉宾
@login_required
def guest_delete(request, eid):
	guest = Guest.objects.filter(id=eid)
	if not guest:
		messages.error(request, '数据不存在')
		response = HttpResponseRedirect('/guest_manage/')
		return response
	else:
		guest.delete()
		response = HttpResponseRedirect('/guest_manage/')
		return response

# 新增嘉宾页面
@login_required
def guest_insert_index(request):
	return render(request, 'guest_insert_index.html')

# 新增嘉宾动作
@login_required
def guest_insert_action(request):
	phone = request.POST.get('phone', '')
	email = request.POST.get('email', '')
	realname = request.POST.get('realname', '')
	event_id = request.POST.get('event_id', '')
	create_time = datetime.now()
	sign = '0'
	try:
		new_guest = Guest.objects.create(realname=realname, phone=phone, email=email, sign=sign, event_id=event_id, create_time=create_time)
	except:
		new_guest = {}
	if new_guest:

		return render(request, 'guest_insert_index.html', {'guest': new_guest, 'hint':'嘉宾新增成功'})
	else:
		return render(request, 'guest_insert_index.html', {'guest': new_guest, 'hint': '嘉宾新增失败了'})