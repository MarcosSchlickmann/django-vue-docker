from django.db import models

# Create your models here.


class Event(models.Model):

    class Meta:

        db_table = 'event'

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_date_time = models.DateTimeField(blank=True, null=True)
    finish_date_time = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title