
from django.http import request
from django.urls import path
from .import views
urlpatterns =[
    path('',views.home,name="home"),
    path('user_login',views.user_login,name="user_login"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('holi_req',views.holi_req,name="holi_req"),
    path('holi_app',views.holi_app,name="holi_app"),
]
