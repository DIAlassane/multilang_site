from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    publication_date = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ['-date_added']