"""定义learning_logs的url模式"""
from django.conf.urls import url
from django.urls import path,re_path

from . import views

urlpatterns = [
    # 主页
    path('index/',views.index,name='index'),
    # 主题
    path('topics/',views.topics,name='topics'),
    # 主题条目
    re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
]