from django.db import models

# Create your models here.
class IndexContent (models.Model):
    title = models.TextField()
    lower_text = models.TextField()
    upper_text = models.TextField()