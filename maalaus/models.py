import datetime
from django.db import models
from django.utils import timezone

class Homepage(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # def was_published_recently(self):
    #     return self.date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.text

class EmailPage(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    # def was_published_recently(self):
    #     return self.date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.email
