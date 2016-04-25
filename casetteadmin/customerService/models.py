from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    customer_identifier = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=20)
    personal_identifier = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' (' + self.customer_identifier + ')'

