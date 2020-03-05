'''
serializers用于定义API的表现形式，如返回哪些字段，返回怎样的格式等。
这里序列化Django自带的User和Group
'''

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Guest, Event

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class EventSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Event
		fields = ('url', 'name', 'address', 'start_time', 'limit', 'status')

class GuestSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Guest
		fields = ('url', 'realname', 'phone', 'email', 'sign', 'event')