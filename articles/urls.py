from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    # path('article_list/', views.article_list),
    path('article_details/<slug>', views.article_details, name="details")
]