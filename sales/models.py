from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)

class ProductInfo(models.Model):
    styleId=models.CharField(max_length=32)
    styleName=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    desc=models.CharField(max_length=320)
    image=models.URLField()
    lastEdit=models.DateField()

class ProductPropImg(models.Model):
    id=models.IntegerField(primary_key=True)
    styleId=models.CharField(max_length=32)
    props=models.CharField(max_length=32)
    url=models.URLField()
    position=models.IntegerField()

class ProductImg(models.Model):
    id=models.IntegerField(primary_key=True)
    sku=models.CharField(max_length=32)
    image=models.URLField()
    position = models.IntegerField()





