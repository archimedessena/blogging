from django.urls import path

from blogs.views import home, BestContentList

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', BestContentList.as_view()),


]