from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages


def login(request):
    return render(request, 'loginpage.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username:
            try:
                check_username = USER_DATA.objects.get(u_name=username)
                if check_username and check_username.password == password:
                    print('login')
                    messages.success(request, f'login {check_username.u_name}')
                    return HttpResponse(f'welcome {check_username}')
                else:
                    print('[-] Your username or password is wrong')
                    messages.info(request, '[-] Your username or password is wrong')
                    return redirect('/')


            except:
                messages.info(request, '[-] user not found ')
                print(' [-] user not found ')
                return render(request, 'loginpage.html')
        else:
            print(' [-] write your username')
            messages.info(request, '[-] write your username')

    return render(request, 'loginpage.html')


def signuppage(request):
    return render(request, 'signup.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        check_username = USER_DATA.objects.filter(u_name=username)
        if check_username:
            print(' [-] already registerd you have to choose another one')
            messages.success(request, '[-] already registerd you have to choose another one')

            return render(request, 'signup.html')
        else:
            data = USER_DATA.objects.create(u_name=username, password=password)
            data.save()
            print(' [+] You have successfully registered')
            messages.success(request, '[+] You have successfully registered')
            return render(request, 'loginpage.html')


def reset_page(request):

    return render(request, 'forgetpass_page.html')


def reset_pass(request):
    if request.method == "POST":
        username = request.POST['username']
        new_password = request.POST['password']
        try:
            check_username = USER_DATA.objects.get(u_name=username)
            if check_username:
                check_username.password = new_password
                check_username.save()
                messages.success(request, 'Password successfully reset.')
                print(new_password)
                return redirect('/')
            else:
                print(" [-] user doesn't exist ")

        except:
            messages.info(request, '[-] user not found')

            print(' [-] user not found')
            return render(request, 'forgetpass_page.html')
