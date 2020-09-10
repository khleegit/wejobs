from django.shortcuts import render,  get_object_or_404
from django.utils import timezone
from .models import Post, Classifications, Categorys
from .forms import PostForm, classificationSaveForm, CategorySaveForm
#from .models import Plan
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse


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
    #filt = Plan.objects.filter()
    #plans = filt.values('classification').order_by('classification').distinct()
    return render(request, 'fmjobs/targetregistration.html', {})


def targetsetting(request):
    #plans = Plan.objects.all()
    return render(request, 'fmjobs/targetsetting.html', {})


def classification(request):
    classifications = Classifications.objects.order_by('classification')
    return render(request, 'fmjobs/classification.html', {'classifications': classifications})


def classification_new(request):
    if request.method == "POST":
        form = CategorySaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classification')
        else:
            return HttpResponse("에러가 발생했습니다.")
    else:
        form = classificationSaveForm()
        
    return render(request, 'fmjobs/classification_new.html', {'form' : form})


def classification_edit(request, pk):
    classification = get_object_or_404(Classifications, pk=pk)
    if request.method == "POST":
        form = classificationSaveForm(request.POST, instance = classification)
        if form.is_valid():
            form.save()
            return redirect('classification')
    else:
        form = classificationSaveForm(instance = classification)
    return render(request, 'fmjobs/classification_edit.html', {'form': form})


def classification_remove(request, pk):
    classification = get_object_or_404(Classifications, pk=pk)
    classification.delete()
    return redirect('classification')
    

def category(request):
    categorys = Categorys.objects.all()
    return render(request, 'fmjobs/category.html', {'categorys':categorys})


def category_new(request):
    clfc = Classifications.objects.order_by('classification')
    if request.method == "POST":
        form = CategorySaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
        else:
            return HttpResponse("에러가 발생했습니다.")
    else:
        form = CategorySaveForm()
        
    return render(request, 'fmjobs/category_new.html', {'form' : form, 'clfc' : clfc})


def category_edit(request, pk):
    ce = get_object_or_404(Categorys, pk=pk)
    if request.method == "POST":
        form = CategorySaveForm(request.POST, instance = ce)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategorySaveForm(instance = ce)
    return render(request, 'fmjobs/category_edit.html', {'form': form})


def category_remove(request, pk):
    cr = get_object_or_404(Categorys, pk=pk)
    cr.delete()
    return redirect('category')



        
def crud(request):
    return render(request, 'fmjobs/crud.html', {})


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


