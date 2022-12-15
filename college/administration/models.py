from django.db import models


# Create your models here.
class Admin(models.Model):
    position = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"

    def __str__(self):
        return self.position


class Administration(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='admins')
    position = models.ForeignKey("Admin", on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Administration"
        verbose_name_plural = "Administrations"

    def __str__(self):
        return f"{self.name} ({self.position})"
