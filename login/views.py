from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.admin import User


# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                return render_to_response('housefinance/index.html', {'username': username})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response(template_name='login/login.html', context={'uf': uf})