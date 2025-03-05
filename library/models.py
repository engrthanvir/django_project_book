from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    publish_date = models.DateField()
    genre = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"
