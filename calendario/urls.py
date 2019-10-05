from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *
from . import views
from CEM.views import permisoDenegado

urlpatterns = [
   # path('calendario/', index, name='inicioCalendario'),
   url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
   url(r'^event/new/$', views.event, name='event_new'),
   url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
   url(r'^event/detail/(?P<event_id>\d+)/$', views.eventDetail, name='event_detail'),
   path('event/<int:event_id>/eliminar/', views.eventoEliminar, name='event_eliminar'),
   path('event/permisoDenegado/', permisoDenegado, name='permisos'),
]