from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('article_detials/', views.article_details)
]
