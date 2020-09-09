from django.shortcuts import render
from django.views.generic import ListView
from blogs.models import Post

# Create your views here.
def home(request):
    #context = {
    #    'posts': Post.objects.all()
    #}
    return render(request, 'blogs/home.html')
    #context)


class BestContentList(ListView):
    queryset = Post.objects.order_by('-date_posted')
    context_object_name = 'posts'
    template_name = 'blogs/bestcontentlist.html'


class BlogList(ListView):
    queryset = Post.objects.order_by('-date_posted')
    context_object_name = 'posts'
    template_name = 'blogs/blog.html'




