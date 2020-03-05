from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.seriazlizers import UserSerializer, GroupSerializer, EventSerializer, GuestSerializer
from django.shortcuts import render
from api.models import Guest, Event

# Create your views here.

# ViewSets定义视图的展示形式
class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class EventViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Event.objects.all()
	serializer_class = EventSerializer


class GuestViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Guest.objects.all()
	serializer_class = GuestSerializer