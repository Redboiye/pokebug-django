from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    type = models.CharField(max_length=32)
    picture = models.URLField(null=False)
    video = models.TextField(null=True)

    def __str__(self):
        return self.title
