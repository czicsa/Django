from django.db import models

class SystemSetting(models.Model):
    resource_key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.resource_key
