from email.policy import default
from django.db import models

class Articles(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now=True)
    thumb=models.ImageField(default='default.png', blank=True)
    # Add in author later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+"..."

# To make migration file to track the change in models
#  python manage.py makemigrations
#  python manage.py migrate