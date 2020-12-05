from django.db import models

# Create your models here.


class Record(models.Model):
    datetime = models.CharField(max_length=50, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'record'
