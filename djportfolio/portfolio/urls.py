from django.urls import path

from .views import (
    ProjectDetailView,
    ProjectListView,

)

app_name = 'Posts'
urlpatterns = [
    path('', ProjectListView.as_view(), name='Project-list'),
    path('<slug:slug>/', ProjectDetailView.as_view(), name='Project-detail'),
]
