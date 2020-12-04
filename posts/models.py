from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True, null=True)
    keywords = models.CharField(max_length=50)
    comments = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    author = models.IntegerField(blank=True, null=True)
    thumbs = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=300, blank=True, null=True)
    head = models.CharField(max_length=700, blank=True, null=True)
    resolved = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Posts'
