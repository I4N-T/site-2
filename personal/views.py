from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'personal/about.html')

def about(request):
    return render(request, 'personal/about.html')

def projects(request):
    return render(request, 'personal/projects.html')

def contact(request):
    return render(request, 'personal/contact.html')

def blog(request):
    return render(request, 'personal/blog.html')

def blog_posts(request, post_id):
    urlText = 'personal/posts/' + post_id + '.html'
    return render(request, urlText)

def proj(request, proj_id):
    urlText = 'personal/demo/' + proj_id + '.html'
    return render(request, urlText)
    
    
        

