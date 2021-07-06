from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import User_Post

# Create your views here.

def home(request):
    posts = User_Post.objects.all()
    return render(request,'home.html',{'posts':posts})


def post_detail(request,id):
    posts = User_Post.objects.get(id=id)
    return render(request,'blog_detail.html',{'posts':posts})


def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Successfully')
            return redirect('login')
        else:
            messages.error(request,'check your registration Value!!')
            # return redirect('signup')

    fm = SignupForm()

    return render(request,'signup.html',{'form':fm})




def user_login(request):
    if request.method == 'POST':
        fm = LoginForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            psw = fm.cleaned_data['password']

            user = authenticate(username=uname,password=psw)

            if user is not None:
                login(request,user)
                messages.success(request,'Login Successfully')
                return redirect('home')
    else:
        fm = LoginForm()
    return render(request,'login.html',{'form':fm})


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')



def user_post(request):

    if request.method == 'POST':

        user = request.user
        text = request.POST['content']
        obj = User_Post(user=user,text=text)
        obj.save()
        return redirect('home')
    else:
        return render(request,'user_post.html')



