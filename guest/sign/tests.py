from django.test import TestCase
from datetime import datetime
from sign.models import Event, Guest
from django.contrib.auth.models import User
# Create your tests here.


class ModelTest(TestCase):
	'models类测试'
	def setUp(self):
		tnow = datetime.now()
		print(tnow)
		Event.objects.create(id=1, name='xiaomi11-pro', limit=2000, address='上海浦东', status='0', start_time='2020-03-03 10:27:24', create_time='2020-03-03 10:27:24')
		Guest.objects.create(id=1, event_id=1, phone='14599999999', realname='xiaomi11-proguest', email='44@33.com', sign='0', create_time='2020-03-03 10:27:24')


	def test_event_models(self):
		result = Event.objects.get(name='xiaomi11-pro')
		self.assertEqual(result.address, '上海浦东')
		self.assertTrue(result.status)

	def test_guest_models(self):
		result = Guest.objects.get(phone='14599999999')
		self.assertEqual(result.realname, 'xiaomi11-pro')
		self.assertFalse(result.sign)


class IndexPageTest(TestCase):
	'测试index登陆页(视图测试)'

	def test_index_page_renders_index_template(self):
		response = self.client.get('/index/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):
	'测试登陆动作'
	def setUp(self):
		User.objects.create_user('admin', 'admin@admin.com', 'admin123456')

	def test_add_admin(self):
		'测试添加用户'
		user = User.objects.get(username = 'admin')
		self.assertEqual(user.username, 'admin')
		self.assertEqual(user.email, 'admin@admin.com')

	def test_login_action_username_password_null(self):
		'用户名密码为空'
		test_data = {'username':'', 'password':''}
		response = self.client.post('/login_action/', data=test_data)
		self.assertEqual(response.status_code, 200)
		self.assertIn('username or password error', response.content)

	def test_login_action_username_password_error(self):
		'用户名密码错误'
		test_data = {'username':'abc', 'password':'123'}
		response = self.client.post('/login_action/', data=test_data)
		self.assertEqual(response.status_code, 200)
		self.assertIn('username or password error', response.content)

	def test_login_action_sucess(self):
		'登陆成功'
		test_data = {'username':'admin', 'password':'admin123456'}
		response = self.client.post('/login_action/', data=test_data)
		self.assertEqual(response.status_code, 302)


class EventManageTest(TestCase):
	'发布会管理'
	def setUp(self):
		User.objects.create_user('admin', 'admin@admin.com', 'admin123456')
		Event.objects.create(id=1, name='xiaomi11-pro', limit=2000, address='上海浦东', status='0', start_time='2020-03-03 10:27:24', create_time='2020-03-03 10:27:24')
		self.login_user = {'username':'admin', 'password':'admin123456'}

	def test_event_manage_sucess(self):
		'测试发布会：xiaomi11-pro'
		response = self.client.post('login_action', data = self.login_user)
		response = self.client.post('/event_manage/')
		self.assertEqual(response.status_code, 200)
		sekf.assertIn('xiaomi11-pro', response.content)
		self.assertIn('上海浦东', response.content)

class GuestManageTest(TestCase):
	'嘉宾管理'
	def setUp(self):
		User.objects.create_user('admin', 'admin@admin.com', 'admin123456')
		Event.objects.create(id=1, name='xiaomi11-pro', limit=2000, address='上海浦东', status='0', start_time='2020-03-03 10:27:24', create_time='2020-03-03 10:27:24')
		Guest.objects.create(id=1, event_id=1, phone='14599999999', realname='xiaomi11-proguest', email='44@33.com', sign='0', create_time='2020-03-03 10:27:24')
		self.login_user = {'username':'admin', 'password':'admin123456'}

	def test_event_manage_sucess(self):
		'测试嘉宾信息'
		response = self.client.post('login_action', data = self.login_user)
		response = self.client.post('/guest_manange/')
		self.assertEqual(response.status_code, 200)
		sekf.assertIn('xiaomi11-progugest', response.content)
		self.assertIn('1459999999914599999999', response.content)

class SignIndexActionTest(self):
	'发布会签到'
	def setUp(self):
		User.objects.create_user('admin', 'admin@admin.com', 'admin123456')
		Event.objects.create(id=1, name='xiaomi11-pro', limit=2000, address='上海浦东', status='0', start_time='2020-03-03 10:27:24', create_time='2020-03-03 10:27:24')
		Guest.objects.create(id=1, event_id=1, phone='14599999999', realname='xiaomi11-proguest', email='44@33.com', sign='0', create_time='2020-03-03 10:27:24')
		self.login_user = {'username':'admin', 'password':'admin123456'}

	def test_sign_index_action_phone_null(self):
		'手机号为空'
		response = self.client.post('/login_action', data=self.login_user)
		response = self.client.post('/sign_index_action/1/', {'phone':""})
		self.assertEqual(response.status_code, 200)
		self.assertIn('phone error', response.content)

