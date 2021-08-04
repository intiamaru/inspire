
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
from .models import Project

# Create your views here.

class ProjectListView(ListView):
    template_name = 'portfolio/project_list.html'
    queryset = Project.objects.all() # <blog>/<modelname>_list.html

class ProjectDetailView(DetailView):
    template_name = 'portfolio/project_detail.html'

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Project, slug=slug_)
