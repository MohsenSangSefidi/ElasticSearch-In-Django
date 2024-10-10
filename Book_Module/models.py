from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.title
