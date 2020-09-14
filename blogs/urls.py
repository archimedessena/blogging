from django.urls import path
from . import views 
from blogs.views import home, BestContentList, BlogList, BlogDetailView, BestContentDetailView
#from .views import BlogDetailView, BestContentDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('bestcontentlist/', BestContentList.as_view()),
    path('bloglist/', BlogList.as_view()),
    path('blogdetailview/<int:pk>/', BlogDetailView.as_view(template_name ='blog_detail.html')),
    path('bestcontentdetail/<int:pk>/', BestContentDetailView.as_view(), name='bestcontent-detail'),
]

