from django.urls import path
from . import views 
from blogs.views import home, BestContentList, BlogList

urlpatterns = [
    path('', views.home, name='home'),
    path('contentlist/', BestContentList.as_view()),
    path('blog/', BlogList.as_view()),


]

