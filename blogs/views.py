from django.shortcuts import render, get_object_or_404
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
    template_name = 'blogs/bloglist.html'


class BlogDetailView(DetailView):
    model = Blog.objects.order_by('-date_posted')
    template_name = 'blogs/blog_detail.html'




