from django.db import models

import typeService.models as Types
import customerService.models as Customers


class Media(models.Model):
    media_title = models.CharField(max_length=200)
    purchase_date = models.DateField()
    rented_date = models.DateField(null=True)
    seq = models.CharField(max_length=20, unique=True)
    media_type = models.OneToOneField(Types.Type, related_name="media_type")
    status_type = models.OneToOneField(Types.Type, related_name="media_status_type")
    is_deleted = models.BooleanField(default=False)
    customer = models.ForeignKey(Customers.Customer, related_name="medias", null=True)

    def __str__(self):
        return self.media_title