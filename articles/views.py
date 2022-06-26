from django.shortcuts import render

import articles

def article_list(request):
    return render(request, "articles/articles_list.html")

def article_detials(request):
    return render(request, "articles/article_details.html")