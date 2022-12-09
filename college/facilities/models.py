from django.db import models


# Create your models here.
class FacilityType(models.Model):
    type = models.CharField(max_length=100)

    class Meta:
        verbose_name = "facility type"
        verbose_name_plural = 'facility types'

    def __str__(self):
        return self.type


class Facility(models.Model):
    name = models.CharField(max_length=100)
    facility_type = models.ForeignKey('FacilityType', on_delete=models.CASCADE)
    info = models.TextField()
    image_field = models.FileField(upload_to='facility')

    class Meta:
        verbose_name = "facility"
        verbose_name_plural = 'facilities'

    def __str__(self):
        return self.name
