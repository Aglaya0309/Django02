from django.shortcuts import render
from .models import News_post
# Create your views here.

def home(request):
    news = News_post.objects.all().order_by('-pub_date')
    return render (request, 'news/news.html', {"news" : news})

