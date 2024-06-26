from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.hashers import make_password
user = get_user_model()

class user_login(View):
    def get(self, request):
        return render(request, 'accaunt/login.html')
    
    def post(self, request):
        username  = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
           login(request, user)
           messages.success(request, "Login .")
           return redirect('home_page')
        else:
            messages.error(request, "Login qilinmadi")
            return render(request, 'accaunt/login.html')


class user_register(View):
    def get(self, request):
        return render(request, 'accaunt/login.html')
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username  = request.POST.get('username')
        password = request.POST.get('password')
        repeatPassword = request.POST.get('repeatPassword')
        
        if password == repeatPassword:
            
            try:
                user.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=make_password(password)
            )
            except Exception as e:
                print(f'xato --- {e}')
                
                
            newUser = authenticate(username=username, password=password)
            print(newUser)
            if newUser is not None:
                login(request, newUser)
               
                return redirect('home_page')
            else:
                messages.error(request, "ro'yhatdan o'tmadi")
                return render(request, 'accaunt/login.html')

        return redirect('home_page')
def user_logout(request):
    logout(request)
    
    return redirect('user_login')


def user_profile(request):
    pass