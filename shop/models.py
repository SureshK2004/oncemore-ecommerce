from django.db import models
from datetime import datetime
import os

def getFilename(request, filename):
    now_time = datetime.now().strftime("%Y%m%d%H%M%S")  # Corrected time format
    new_filename = f"{now_time}_{filename}"  # Using f-string for better readability
    return os.path.join('uploads/', new_filename)

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    image=models.ImageField(upload_to=getFilename,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Products(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=False,blank=False)
    vendor=models.CharField(max_length=100,null=False,blank=False)
    product_image=models.ImageField(upload_to=getFilename,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-trending")
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name