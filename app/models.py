from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.CharField(max_length=120)
    pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title