from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLPattern
from django.views.generic.base import TemplateView
from .views import AllListView, RegisterReserveView, ReserveDetailView, WritingLogView, UpdateLogView, DeleteLogView, DeleteReserveView, writingthisresrvelog, registerreserve
from django.contrib.auth import views as auth_views


app_name = 'reserving'
urlpatterns = [
    path('alllist/', AllListView.as_view(), name="alllist"),
    path('reserve/<int:pk>/', ReserveDetailView.as_view(), name='reserve_detail'),
    path('register/reserve/', RegisterReserveView.as_view(), name='registerreserve'),
    path('writing/log', WritingLogView.as_view(), name='writinglog'),
    path('update/log/<int:pk>/', UpdateLogView.as_view(), name='updatelog'),
    path('delete/log/<int:pk>/', DeleteLogView.as_view(), name='deletelog'),
    path('delete/reserve/<int:pk>/', DeleteReserveView.as_view(), name='deletereserve'),
    path('writing/reserve/log/<int:pk>', writingthisresrvelog, name='writingthisreservelog'),
]
