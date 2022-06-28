from django.http import HttpResponse
from django.shortcuts import render

def signup_view(request):
    return render(request, 'accounts/signup.html')
