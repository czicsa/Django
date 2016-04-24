from django.db import models

import typeService.models as Types


class Media(models.Model):
    media_title = models.CharField(max_length=200)
    purchase_date = models.DateField()
    media_type = models.ForeignKey(Types.Type, related_name="media_type")
    status_type = models.ForeignKey(Types.Type, related_name="media_status_type")

    def __str__(self):
        return self.media_title