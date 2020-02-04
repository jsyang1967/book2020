from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField()
    is_online = models.NullBooleanField(default=True)

    def __str__(self):
        return self.name
