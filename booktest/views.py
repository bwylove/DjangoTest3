# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    return HttpResponse('hello world')


def detail(request,p1):
    return HttpResponse(p1)

# def show(*args,**kwargs):
# #     # args 以位置对应的  元组
# #     # kwargs 以关键字对应的  字典
def detail2(request,p1,p2,p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))


def detail3(request,p1,p2,p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))
#展示链接的页面
def getTest1(request):
    return render(request,'booktest/getTest1.html')

#展示一键一值的情况
def getTest2(request):
    #根据键接受值
    a1=request.GET['a']
    b1=request.GET['b']
    c1=request.GET['c']
    # 构造上下文
    context={'a':a1,'b':b1,'c':c1}
    # 向模板传递上下文，并进行渲染
    return render(request,'booktest/getTest2.html',context)

#展示一键多值的情况
def getTest3(request):
    a1=request.GET.getlist('a')
    context={'a':a1}
    return render(request,'booktest/getTest3.html',context)


def postTest1(resquest):
    return render(resquest,'booktest/postTest1.html')

def postTest2(resquest):
    uname=resquest.POST['uname']
    upwd=resquest.POST['upwd']
    ugender=resquest.POST['ugender']
    uhobby=resquest.POST.getlist('uhobby')
    context={'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
    return render(resquest,'booktest/postTest2.html',context)

# cookie練習
def cookieTest(request):
    response=HttpResponse()
    # response.set_cookie('t1','abc')
    cookie=request.COOKIES
    if cookie.has_key('t1'):
        response.write(cookie['t1'])
    return response

# 转向练习
def redTest1(request):
    # return HttpResponseRedirect('/booktest/redTest2/')
    return redirect('/booktest/redTest2/')
def redTest2(request):
    return HttpResponse('这是转向的来的页面')

# 通过用户登陆推出练习session
def session1(request):
    uname=request.session.get('myname','未登陆')
    context={'uname':uname}
    return render(request,'booktest/session1.html',context)

def session2(request):
    return render(request,'booktest/session2.html')
def session2_handle(request):
    uname=request.POST['uname']
    request.session['myname']=uname
    # request.session.set_expiry(0)
    return redirect('/booktest/session1/')
def session3(request):
    del request.session['myname']
    return redirect('/booktest/session1')