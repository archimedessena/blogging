from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blogs.models import Post, Blog

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


class BestContentDetailView(DetailView):
    model = Post

    


class BlogList(ListView):
    queryset = Blog.objects.order_by('-date_posted')
    context_object_name = 'entries'
    template_name = 'blogs/blog.html'


class BlogDetailView(DetailView):
    model = Blog




