from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    nationality = models.CharField(max_length=35)
    birthday = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userprofile")
    image = models.ImageField(upload_to="profiles/%Y/%m/%d")

    def __str__(self):
        return self.user.username