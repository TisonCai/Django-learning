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
        print('form is valid or not',form.is_valid())
        print('form is valid or not', form)
        if form.is_valid():
            new_user = form.save()
            user_authenticate = authenticate(username=new_user.username,password=request.POST['password'])
            if user_authenticate is None:
                return HttpResponseRedirect(reverse('users:invalid_register'))
            else:
                login(request,user_authenticate)
                return HttpResponseRedirect(reverse('learning_logs:index'))
        else:
            return HttpResponseRedirect(reverse('users:invalid_register'))

    context = {'form': form}
    return render(request, 'users/register.html', context)



# def register(request):
#     """注册新用户"""
#     if request.method != 'POST': # 显示空的注册表单
#         form = UserCreationForm()
#     else:
#         # 处理填写好的表单
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             usename = request.POST.get('username','')
#             password = request.POST.get('password', '')
#             # 让用户自动登录，再重定向到主页
#             authenticated_user = authenticate(username=usename,password=password)
#             if authenticated_user is None:
#                 return HttpResponseRedirect(reverse('users:invalid_register'))
#             else:
#                 login(request, authenticated_user)
#                 return HttpResponseRedirect(reverse('learning_logs:index'))



def invalid_register(request):
    return render(request,'users/invalid_register.html')

