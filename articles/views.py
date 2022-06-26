from django.shortcuts import render
from .models import Articles

def article_list(request):
    return render(request, "articles/articles_list.html")

def article_details(request):
    articles=Articles.objects.all().order_by('date')
    return render(request, "articles/article_details.html", {'articles': articles})