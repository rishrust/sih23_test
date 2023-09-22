from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .forms import *
from .models import *
# landing page
def home(request):
    if request.user.is_authenticated:

        return redirect("index")
    else:
        return render(request,'landingpage.html')
    


# home page
def index(request):
    if request.user.is_authenticated:
        # items = projects.objects.all()
        latest_items = projects.objects.all().order_by('-id')[:4]
        print(latest_items)
        return render(request,'home.html',{"items":latest_items})
    else:
        return render(request,'landingpage.html')
    
def upload(request):
    if request.method =='POST':
        form = projects_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = projects_form()
        print(form)
    return render(request, 'test_upload.html', {'form' : form})

    # return render(request,'upload.html')







def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username)
            print(password)
            if(User.objects.filter(username=username).exists()):
                username=User.objects.get(username=username).username
                userauth = auth.authenticate(username=username,password=password) ##for verification
                if userauth is not None:
                    auth.login(request,userauth) ##passing login info
                    userid=str(User.objects.get(username=username).id)
                    
                    return redirect('home')
                else:
                    messages.info(request,"Invalid Credentials")
                    return redirect('login')
            else:
                messages.info(request,"User Not Registered")
                return redirect('login')
        return render(request,'login.html')




def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        
    return redirect('home')



def register(request):
    if request.method=='POST':
        if request.POST.get('password')==request.POST.get('passwordr'):
            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username)
            print(password)
           
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists")#message automatically 
                return redirect('register')                      #passed in redirect 
    
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()##creating sving objects
                return redirect('home')
        else:
            messages.info(request,"Password doesnt match")
            return redirect('register')    
    return render(request,'register.html')





def aboutus(request):
    return render(request,'aboutus.html')



def view(request):
    items = projects.objects.all()
    return render(request, 'view.html', {'items': items})
    # return render(request,'view.html')



def project_details(request,item_id):
    proj = projects.objects.get(id=item_id)
    print(proj.project_cover.url)
    return render (request, 'project.html', {'project':proj})