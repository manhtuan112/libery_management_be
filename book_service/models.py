from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    public_date = models.DateField()
    page_num = models.PositiveIntegerField(null=True, default=None)
    description = models.CharField(max_length=2000, null=True, default=None)
    image_url = models.CharField(max_length=600, null=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + self.category
