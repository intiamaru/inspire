from django.urls import path

from .views import (
    PostDetailView,
    PostListView,

)

app_name = 'Posts'
urlpatterns = [
    path('', PostListView.as_view(), name='Post-list'),
    path('<int:id>/', PostDetailView.as_view(), name='Post-detail'),
]
