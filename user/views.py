from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as handle_login,authenticate ,logout as LogoutFunction 
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.files.storage import FileSystemStorage
from django.db.models import Q


from .models import Accounts
# Create your views here.


@login_required()

def home(r):
    if r.method == "POST":
        try:
            post = Post()
            post.caption = r.POST.get('caption')
            post.user = r.user
            post.description = r.POST.get('description')
            post.image = r.FILES['image']

            post.save()
            print(str(post))
            return redirect('home')
        except Exception as e:
            print(str(e))
            return redirect('home')

    data = Post.objects.all()
    # print(r.user)
    user = User.objects.filter(~Q(username = r.user) )
    print(user)
    return render(r,'index.html',{"post":data,'user':user})


def uploaddp(r):
   if r.method == 'POST':
    user = Accounts.objects.get(user = r.user)
    # print(user)
    upload = r.FILES['dp']
    # fss = FileSystemStorage()
    # file = fss.save(upload.name, upload)
    # file_url = fss.url(file)
    user.dp = upload
    user.save()

    return redirect('home')
    




def logout(r):
    LogoutFunction(r)
    return redirect('login')


def signup(r):
    if(r.method == "POST"):
        try:
            user = User()
            user.first_name = r.POST.get('firstname')
            user.last_name = r.POST.get('lastname')
            user.username = r.POST.get('firstname') + r.POST.get('email')
            user.email = r.POST.get('email')
          

            user.set_password(r.POST.get('password'))
            user.is_active = True
            user.is_staff = True
            
            user.save()

            req = r.POST
            acc = Accounts()
            acc.user = User.objects.get(pk=user.id)
            acc.contact = req.get('contact')
            acc.gender = req.get('gender')
            acc.dob = req.get('dob')
            acc.save()

            return redirect(to=login)
        except Exception as e:
            print(str(e))
    return render(r,'signup.html')


def login(r):
    if(r.method == "POST"):
        try:
            user = User.objects.filter(email=r.POST.get('email'))
           
            u = authenticate(r,username = user[0],password = r.POST.get('password'))
            print(u)
            if u is None:
                return render(r , 'login.html')
            else:
                handle_login(r , user = u)
                return redirect('home')

        except Exception as e:
            print(str(e))

    return render(r,'login.html')
