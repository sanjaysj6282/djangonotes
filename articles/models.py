from django.db import models

class Articles(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now=True)
    # Add in thumbnail later
    # Add in author later
    
# To make migration file to track the change in models
#  python manage.py makemigrations
#  python manage.py migrate