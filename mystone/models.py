from django.db import models

# Create your models here.


class Mystone(models.Model):
    f = models.TextField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mystone'