from django.shortcuts import render
from learning_logs.models import Topic

# Create your views here.
def index(request):
    return render(request,'learning_logs/index.html')


def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)


def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')   # 降序排序
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)
