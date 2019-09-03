from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path,re_path

from . import views

urlpatterns = [
    # 登录
    re_path(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    # 注销
    re_path(r'^logout/$',views.logout_view,name='logout'),
    # 注册
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^invalid_register/(?P<form>\d+)/$',views.invalid_register,name='invalid_register2'),
    # 注册失败
    re_path(r'^invalid_register/$', views.invalid_register, name='invalid_register'),

    
]