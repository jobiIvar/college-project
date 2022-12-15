from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    image = models.ImageField(upload_to="events")

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = "Events"

    def __str__(self):
        return self.name


class Moto(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = "Motto"
        verbose_name_plural = "Mottos"

    def __str__(self):
        return self.title


class Notification(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"

    def __str__(self):
        return self.title
