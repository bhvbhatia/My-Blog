from django.shortcuts import render,get_object_or_404,redirect,redirect
from .models import Blog , Comment
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, CommentForm , PostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,'blog/home.html',{'blogs':blogs})

def about(request):
    return render(request,'blog/about.html',{})

def detail(request, pk):
    dblog = get_object_or_404(Blog, pk=pk)
    return render(request,'blog/detail.html',{'dblog':dblog})

def cv(request):
    return render(request,'blog/cv.html',{})

def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, ('You Have Been Logged In!'))
        return redirect('blog:home')
    else:
         messages.success(request,('Error Logging In - Please Try Again..'))
         return redirect('login')
  return render(request, 'blog/login.html')

def logout_view(request):
     logout(request)
     messages.success(request, ('You Have Been Logged Out!'))
     return redirect('blog:about')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('Congrats! You have registered.'))
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def comment_form(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('blog:detail', pk=blog.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog:detail', pk=comment.blog.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:detail', pk=comment.blog.pk)

class CreatePostView(LoginRequiredMixin,CreateView):
      login_url = '/login/'
      redirect_field_name = 'blog/detail.html'

      form_class = PostForm

      model = Blog
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/detail.html'

    form_class = PostForm

    model = Blog


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:home')
