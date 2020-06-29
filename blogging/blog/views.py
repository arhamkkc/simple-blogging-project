from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm,PublishForm
from django.contrib import messages 
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def register(request):
    registered = False
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid:
            user = form.save()
            user.set_password(user.password)
            user.save()
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'please give proper detail')
            return redirect('register')

    else:
        form = PostForm()

    return render(request,'blog/register.html',{'form':form,'registered':registered})


def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        ########### to chechk whtere email is present or not 
        post = User.objects.filter(username = username).first()
        if post == None:
            messages.error(request,'no such email found kindly registere')
            return redirect('login')

        user = auth.authenticate(username = username,password=password)

        if user:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'invalid login! please provide exact detail')
            return redirect('login')

    if request.user.is_authenticated:
        messages.error(request,'you are logged in')
        return redirect('/')
    else:
        return render(request,'blog/login.html')


##logout

def logout(request):
    auth.logout(request)
    return redirect('/')



################for writing somthing
@login_required
def publish_form(request):
    form = PublishForm()
    poster = request.user
    if request.method == 'POST':
        form = PublishForm(request.POST)
        if form.is_valid():
            #niche ka process se curentuser ke data me save hoga
            post_form = form.save(commit=False)
            post_form.author = poster
            post_form.save()
            return redirect('/')
        else:
            messages.error(request,'please all the details correctly')
            return redirect('publish_form')

    else:
        form = PublishForm()
    return render(request,'blog/publish_form.html',{'form':form})


###### for displaying what all the post the authir has written
@login_required
def post_list(request):
    user_list = Post.objects.filter(author = request.user)
    return render(request,'blog/post_list.html',{'user_list':user_list})

# def detail_list(request):
#     post_detail_list = Post.objects.all()
#     return render(request,'blog/detail_list.html',{'post_detail_list':post_detail_list})




####### whe the user click thaht he should see the sepecific pst that he has written
@login_required
def get_post(request,id):
    post = get_object_or_404(Post,pk = id)
    return render(request,'blog/detail_list.html',{'post':post})

###########for deleting that specific post
@login_required
def delete_post(request,id):
    post = Post.objects.get(id = id)
    post.delete()
    return redirect('post_list')


####### fro updating
@login_required
def update(request,id):
    post = Post.objects.get(id = id)
    form = PublishForm(request.POST,instance=post)
    if form.is_valid():
        form.save(commit = True)
        return redirect('post_list')
    return render(request,'blog/update.html',{'post':post})
