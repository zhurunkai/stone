from django.db import models

# Create your models here.


class Users(models.Model):
    phone_number = models.BigIntegerField()
    password = models.CharField(max_length=50)
    sex = models.IntegerField()
    nickname = models.CharField(max_length=300)
    posts = models.TextField(blank=True, null=True)
    head = models.CharField(max_length=700)
    joinposts = models.TextField(blank=True, null=True)
    identity = models.IntegerField()
    contribution = models.IntegerField(blank=True, default=0)
    personality = models.CharField(max_length=100, blank=True, null=True)
    auth = models.IntegerField()
    forbid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Users'
