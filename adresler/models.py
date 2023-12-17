from django.db import models
from datetime import datetime

# Create your models here.

class Adresler(models.Model):

    class Meta:
        db_table = 'adresler'

    id = models.AutoField(primary_key=True)
    sehir = models.CharField(max_length=50, null=False)
    mahalle = models.CharField(max_length=100, null=False)
    sokak = models.CharField(max_length=100, null=False)
    bina = models.CharField(max_length=100, null=False)
    daire = models.CharField(max_length=20, null=False)
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    is_deleted = models.BooleanField(default=False)