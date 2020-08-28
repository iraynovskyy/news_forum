from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ':' + str(self.content)
