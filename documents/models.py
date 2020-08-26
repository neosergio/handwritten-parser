from django.db import models


class Document(models.Model):
    text = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
