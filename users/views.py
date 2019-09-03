from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """用户注册"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            user_authenticate = authenticate(username=new_user.username,password=request.POST.get('password1',''))
            if user_authenticate is None:
                return HttpResponseRedirect(reverse('users:invalid_register'))
            else:
                login(request,user_authenticate)
                return HttpResponseRedirect(reverse('learning_logs:index'))
        else:
            return HttpResponseRedirect(reverse('users:invalid_register'))

    context = {'form': form}
    return render(request, 'users/register.html', context)


def invalid_register(request):
    return render(request,'users/invalid_register.html')

