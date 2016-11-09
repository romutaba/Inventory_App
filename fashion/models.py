from django.db import models
from django.utils import timezone

class Items(models.Model):

    name = models.CharField(max_length=200)
    units = models.IntegerField()
    description = models.TextField()
    purchase_date = models.DateTimeField()

    def purchasedate(self):
        self.purchase_date = timezone.now()
        self.save()



