from django.conf.urls import url
from sign import views_if, views_if_sec

urlpatterns = [
	# sign system interface
	# ex: /api/add_event/
	url('add_event/', views_if.add_event, name='add_event'),
	# ex: /api/add_guest/
	url('add_guest/', views_if.add_guest, name='add_guest'),
	# ex: /api/get_event_list/
	url('get_event_list/', views_if.get_event_list, name='get_event_list'),
	# ex: /api/get_guest_list/
	url('get_guest_list/', views_if.get_guest_list, name='get_guest_list'),
	# ex: /api/user_sign/
	url('user_sign/', views_if.user_sign, name='user_sign'),
	# ex: /api/sec_get_event_list/
	url('sec_get_event_list/', views_if_sec.get_event_list, name='get_event_list'),
	# ex: /api/sec_add_event/
	url('sec_add_event/', views_if_sec.add_event, name='add_event'),
	]
