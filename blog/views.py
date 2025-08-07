from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Post
from django.utils import timezone
# Create your views here.

def post_list(request):
    # d = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    d = Post.objects.all()
    return render(request,'blog/post_list.html',context={'polist':d})
def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'detail':post})

def get_num(request,p):
    print(p)
    return HttpResponse(p)
