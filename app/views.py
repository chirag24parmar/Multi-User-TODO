from django.shortcuts import render ,redirect
from django.http import HttpResponse
#importing django default user creation page
from django.contrib.auth import authenticate, login as loginuser
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm

# Create your views here.

def home(request):
    # print('Hello World')
    # return HttpResponse("Response ")
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form" : form
        }
        return render(request,'login.html' , context=context)
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginuser(request,user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request,'login.html' , context=context)

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        #context is a variable(dictionary) which send html data
        context = {
            # pass key as form and value as form
            "form" : form
        }
        return render(request,'signup.html',context=context)
    else:
        form = UserCreationForm(request.POST)
        context = {
            # pass key as form and value as form
            "form" : form
        }
        # return request.POST
        if form.is_valid():
            #we use from.save for saving the user or who is new registration
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request,'signup.html',context=context)
