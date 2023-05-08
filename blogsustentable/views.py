from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect, get_object_or_404

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def index(request):
    return render(request, 'blog/index.html', {})

def service1(request):
    return render(request, 'blog/service1.html', {})

def service2(request):
    return render(request, 'blog/service2.html', {})

def service3(request):
    return render(request, 'blog/service3.html', {})


# def post_list(request):
#     return render(request, 'blog/post_list.html', {})

def noticias(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/noticias.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST , request.FILES) 
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.cover = request.FILES['cover']
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blogsustentable/post_edit.html', {'form': form})

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
    return render(request, 'blogsustentable/post_edit.html', {'form': form})


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('noticias')