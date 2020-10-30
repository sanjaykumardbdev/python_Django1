from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,"Invalid credential")
            return redirect('login')
    else:
        # return render(request, 'register.html')
        # return redirect('/')
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if username == '':
            messages.info(request, "Username required")
            print('Username required')
            return redirect('register')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("Username already exists")
                messages.info(request,"Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request, "Email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('login')
            print("User Created")
            messages.info(request, "User Created")

        else:
            print("Password not matched")
            messages.info(request, "Password not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')
