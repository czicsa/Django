from django.db import models

class Category(models.Model):
    resource_key = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

class Type(models.Model):
    category = models.ForeignKey(Category, related_name="category")
    resource_key = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description
