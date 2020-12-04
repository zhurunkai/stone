from django.db import models

# Create your models here.


class Feedback(models.Model):
    content = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=30, blank=True, null=True)
    star = models.IntegerField(blank=True, null=True)
    annex = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'feedback'