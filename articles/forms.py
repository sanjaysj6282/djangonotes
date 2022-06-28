from django.forms import ModelForm
from . import models

class CreateArticle(ModelForm):
    class Meta:
        model = models.Articles
        # field = '__all__' 
        fields = ['title', 'body', 'slug', 'thumb']