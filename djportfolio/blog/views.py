
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

#from .forms import ArticleModelForm
from .models import Post

# Create your views here.

class PostListView(ListView):
    template_name = 'blog/post_list.html'
    queryset = Post.objects.all() # <blog>/<modelname>_list.html

class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)
