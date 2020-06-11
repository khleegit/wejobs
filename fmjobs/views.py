from django.shortcuts import render,  get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .models import Plan
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.


def post_blank(request):
    return render(request, 'fmjobs/post_blank.html', {})

def login(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return redirect('post_list')
            else:
                return render(request, 'fmjobs/login.html',{'error' : 'username or password is incorrect'})
        else:
            return render(request, 'fmjobs/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('login')

def weplan(request):
    return render(request, 'fmjobs/weplan.html', {})

def dashboard(request):
    return render(request, 'fmjobs/dashboard.html', {})

def targetregistration(request):
    return render(request, 'fmjobs/targetregistration.html', {})

def targetsetting(request):
    plans = Plan.objects.all()
    return render(request, 'fmjobs/targetsetting.html', {'plans': plans})

def affiliate(request):
    return render(request, 'affiliate/index.html', {})

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'fmjobs/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'fmjobs/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'fmjobs/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'fmjobs/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def home(request):
    return render(request, 'fmjobs/home.html', {})

def webfiction(request):
    return render(request, 'fmjobs/webfiction.html', {})

def uncapitalizedstartup(request):
    return render(request, 'fmjobs/uncapitalizedstartup.html', {})

def digitalnomad(request):
    return render(request, 'fmjobs/digitalnomad.html', {})
