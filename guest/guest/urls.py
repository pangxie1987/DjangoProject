"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sign import views
from django.conf.urls import url
urlpatterns = [
	path('', views.index),
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login_action/', views.login_action),
    path('event_manage/', views.event_manage),
    path('accounts/login/', views.index),
    path('search_name/', views.search_name),
    path('guest_manage/', views.guest_manage),
    path('search_name_guest/', views.search_name_guest),
    url('sign_index/(?P<eid>[0-9]+)/', views.sign_index),
    #path('sign_index/2/', views.sign_index),
    url('sign_index_action/(?P<eid>[0-9]+)/', views.sign_index_action),
    path('logout/', views.logout),
    url('event_insert_guest_index/(?P<eid>[0-9]+)/', views.event_insert_guest_index),
    url('event_insert_guest_action/(?P<eid>[0-9]+)/', views.event_insert_guest_action),
    url('event_insert_index/', views.event_insert_index),
    url('event_insert_action/', views.event_insert_action),
    url('event_update_index/(?P<eid>[0-9]+)/', views.event_update_index),
    url('event_update_action/(?P<eid>[0-9]+)/', views.event_update_action),
    url('event_delete/(?P<eid>[0-9]+)/', views.event_delete),
    url('guest_update_index/(?P<eid>[0-9]+)/', views.guest_update_index),
    url('guest_update_action/(?P<eid>[0-9]+)/', views.guest_update_action),
    url('guest_delete/(?P<eid>[0-9]+)/', views.guest_delete),
    url('guest_insert_index/', views.guest_insert_index),
    url('guest_insert_action/', views.guest_insert_action),
]
