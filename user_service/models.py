from django.db import models
import uuid

# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    dateOfBirth = models.DateField()

    def __str__(self):
        return self.name + self.username
