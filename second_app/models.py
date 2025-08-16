from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    email = models.CharField(max_length=128)
    role = models.CharField(max_length=5, default="user")

    def __str__(self):
        return self.username

class Group(models.Model):
    name = models.CharField(64)
    users = models.ManyToManyField(User, related_name='groups')

    def __str__(self):
        return self.name


