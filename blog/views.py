from django.shortcuts import render,HttpResponse
from .models import Post
from django.utils import timezone
# Create your views here.

def post_list(request):
    # d = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    d = Post.objects.all()
    return render(request,'blog/post_list.html',{'data':d})

