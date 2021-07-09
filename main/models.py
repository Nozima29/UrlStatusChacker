from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UrlModel(models.Model):
    user = models.ForeignKey(User, related_name='user_url', on_delete=models.CASCADE)
    url = models.URLField()
    status_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.url