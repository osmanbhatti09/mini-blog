from django.shortcuts import render, HttpResponseRedirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm 
from .forms import LogInForm, PostForm
from django.contrib.auth import authenticate, logout ,login 
from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect
# Create your views here.
#For Home page

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def dashboard(request):
    posts = Post.objects.all()
    user = request.user               ##making this to get data from group user name
    # # full_name = user.get_full_name          ##get full name of the groups from admin page
    # full_name = user.get_full_name()
    # group_name = user.groups.all()        ##get also groups names with user that makes on admin page
    return render(request, 'blog/dashboard.html', {'posts':posts})

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
           messages.success(request, 'You have successfully created your Account, Congratulation!! ')
           user = form.save()
           form = SignUpForm()
           group = Group.objects.get(name='public')  ##This group is for to allow admin models groups to make changes as per we selected in admin
           user.groups.add(group)      #then group variable add in that user that make above #groups represents which we made in admin page
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form':form})

## **import query (why request=request "put" data=request.Post)**
def user_login(request):
    # if not request.user.is_authenticated:
  if  request.method == 'POST':
    form = LogInForm(request=request, data = request.POST)   
    if form.is_valid():
        unam = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user = authenticate(username=unam, password=upass)
        if user is not None:
            request.session['userInfo'] = unam
            login(request, user)
            messages.success(request,'You Enter right information successfully login!!')
            return HttpResponseRedirect('/dashboard/') 
  else:
    form = LogInForm()
  return render(request, 'blog/login.html', {'form':form})
    # else:
    #   return HttpResponseRedirect('/dashboard/')  ##because if he already login then we will route him to direct dashboard page

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
              ttl = form.cleaned_data['title']
              cont = form.cleaned_data['content']
              frm = Post(title=ttl, content=cont)
              frm.save()
              messages.success(request,"Post has been added successfully!!!")
              form =PostForm()
        else:
          form = PostForm()         
        return render(request, 'blog/addpost.html', {'form':form})
    else: 
      return HttpResponseRedirect('/login/')
def update_post(request, id):
    if request.user.is_authenticated:
      if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        form = PostForm(request.POST, instance=id)
        if form.is_valid():
          form.save()
          messages.success(request, 'Finally You edited your posr successfully!!!')
          PostForm()
      else:
        pi = Post.objects.get(pk=id)
        form = PostForm(instance=id)
      return render(request, 'blog/updatepost.html', {'form':form})
    else:
      return HttpResponseRedirect('/login/')
    

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect( '/dashboard/')     
    else:
      return HttpResponseRedirect('/login/')