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
    # 添加新主题的网页
    re_path(r'^new_topic/$',views.new_topic,name='new_topic'),
    # 添加新学习条目
    re_path(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    # 编辑学习条目
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]