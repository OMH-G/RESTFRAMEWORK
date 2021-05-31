from django.db import models
# Create your models here.
class Scheme(models.Model):
    id=models.AutoField(primary_key=True)
    scheme_code=models.CharField(max_length=6,default='')
    scheme_info=models.CharField(max_length=250,default='')