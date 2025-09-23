from django.shortcuts import render, get_object_or_404
from ..models import Post
 
 
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})
 
 
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail1.html', {'post': post})
 