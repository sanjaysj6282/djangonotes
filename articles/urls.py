from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('article_list/', views.article_list),
    path('article_details/<slug>', views.article_details)
]