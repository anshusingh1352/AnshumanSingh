from django.db import models

# Create your models here.
class sendmail(models.model):
    email =models.CharField(max_length =122)
    code =models.CharField(max_length =122)
