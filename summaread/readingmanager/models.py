from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Summary(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='book',
    )
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300)
    start = models.IntegerField()
    end = models.IntegerField()
    summary = models.TextField()

    class Meta:
        verbose_name_plural = "summaries"
