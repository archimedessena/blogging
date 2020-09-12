from django.urls import path
from . import views 
from blogs.views import home, BestContentList, BlogList
from .views import BlogDetailView, BestContentDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('bestcontentlist/', BestContentList.as_view()),
    path('bloglist/', BlogList.as_view()),
    path('blogdetail/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('bestcontentdetail/<int:pk>/', BestContentDetailView.as_view(), name='bestcontent-detail'),



]

