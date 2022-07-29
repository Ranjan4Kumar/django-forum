from django.db import models


class App(models.Model):
    class Meta(object):
        db_table= 'app'
    name = models.CharField(
        'Name', blank=False, null='False', max_length=14, db_index=True
    )
    body = models.CharField(
        'Body', blank=True, null= True, max_length=140, db_index=True
    )
    created_at= models.DateTimeField(
        'created datetime',blank=True,auto_now_add=True
    )
# Create your models here.
