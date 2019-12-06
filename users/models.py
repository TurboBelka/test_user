from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True,
                              upload_to="static/user_photo")
    age = models.IntegerField()

    def __str__(self):
        return self.user.username

    def is_adult(self):
        return self.age >= 18
