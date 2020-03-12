from locust import TaskSet, HttpLocust, task

class UserBehavior(TaskSet):
	@task
	def baidu_page(self):
		self.client.get('/')

class WebsiteUser(HttpLocust):
	task_set=UserBehavior
	min_wait=5000
	max_wait=5000