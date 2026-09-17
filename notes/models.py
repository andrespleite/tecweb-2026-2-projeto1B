from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.title}"


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='')
    tags = models.ManyToManyField(Tag, blank=True)