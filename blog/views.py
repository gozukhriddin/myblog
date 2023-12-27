from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blog
# Create your views here.
class BlogListview(ListView):
    model = Blog
    template_name = "blog.html"
    context_object_name = "blogs"

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogview.html"

# def bloglistview(request):
#     blogs = Blog.objects.all()
#
#     context = {
#         'blogs' : blogs,
#     }
#     return render(request, 'blog.html', context=context)
#
# def blogview(request,id):
#     blog=get_object_or_404(Blog, id=id)
#     context={
#         "blog":blog
#     }
#     # try:
#     #     blog=Blog.objects.get(id=id)
#     #     context = {
#     #         "blog":blog
#     #     }
#     # except Blog.DoesNotExist:
#     #     raise Http404('Not blog found')
#     return render(request, 'blogview.html', context=context)
#

