from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Post
from posts.forms import PostForm

#def index(request):
#    return HttpResponse(f"Hello, world. You're at the post index.")

class PostList(generic.ListView):
    queryset = Post.objects.order_by('-pub_date') #.filter(status=1)
    template_name = 'index.html'

def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post_author = request.user
            obj.save()
            #login(request, user)
            return redirect('/posts')
    else:
        form = PostForm()
    return render(request, 'posts/add.html', {'form': form})