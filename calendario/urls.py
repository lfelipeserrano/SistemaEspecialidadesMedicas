from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *
from . import views

urlpatterns = [
   path('calendario/', index, name='inicio'),
   url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
   url(r'^event/new/$', views.event, name='event_new'),
   url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit')
]