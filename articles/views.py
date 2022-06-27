from django.http import HttpResponse
from django.shortcuts import render
from .models import Articles


def article_list(request):
    articles=Articles.objects.all().order_by('date')
    return render(request, "articles/articles_list.html", {'articles': articles})

def article_details(request, slug):
    return HttpResponse(slug)
    # return render(request, "articles/article_details.html")