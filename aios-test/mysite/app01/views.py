from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return  HttpResponse("欢迎光临！")

def user_list(request):
    # return HttpResponse("用户列表")
    return render(request,"user_list.html")

def user_add(request):
    return HttpResponse("添加用户")

def aios_login(request):

    return render(request,"aios_login.html")

def baidu(request):
    from django.http import HttpResponseRedirect
    #

    # return render(request,"baidu.html",{"news_list":data_list})
    #return render(request,"baidu.html")

    return HttpResponseRedirect("/login/")

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        print(request.POST)
        print(request.method)
        username = request.POST.get("user")
        password = request.POST.get("pwd")

        if username == "admin" and password == "123":
            #return HttpResponse("登录成功")
            return HttpResponseRedirect("http://www.baidu.com/")
        else:
            #return HttpResponse("登录失败")
            return render(request,"login.html",{"error_msg":"用户名或密码错误"})




