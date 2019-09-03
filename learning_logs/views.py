from django.shortcuts import render
from learning_logs.models import Topic
from .forms import TopicForm,EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
        context = {'form': form}
        return render(request,'learning_logs/new_topic.html',context)
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))


def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
        context = {'form': form,
                   'topic': topic,}
        return render(request,'learning_logs/new_entry.html',context)
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))