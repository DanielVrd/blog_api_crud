from django.db import models

class Article(models.Model):
    author = models.TextField()
    title = models.TextField()
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.title

