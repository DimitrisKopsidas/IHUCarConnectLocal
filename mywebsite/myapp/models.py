from django.db import models

# Create your models here.

class Post(models.Model):
 title = models.CharField(max_length=200)
 content = models.TextField()
 pub_date = models.DateTimeField('date published')