from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class child(models.Model):
    id= models.AutoField(primary_key=True)
    User_id =  models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    First_name = models.CharField(max_length=64, null=True)
    Last_name = models.CharField(max_length=64, null=True)
    Gender = models.CharField(max_length=64, null=True)
    date_of_birth = models.DateField(null=True)
    Organization = models.CharField(max_length=64, null=True)
    Father_name = models.CharField(max_length=64, null=True)
    Father_mobile = models.CharField(max_length=64, null=True)
    Mother_name = models.CharField(max_length=64, null=True)
    State = models.CharField(max_length=64, null=True)
    District = models.CharField(max_length=64, null=True)
    Taluk = models.CharField(max_length=64, null=True)
    Village = models.CharField(max_length=64,null=True)

    def __str__(self):
        return self.First_name

class manual(models.Model):
    child_id =  models.ForeignKey(child, on_delete = models.CASCADE, blank = True, null = True)
    Date = models.DateField(null=True)
    Manual_height = models.CharField(max_length=64, null=True)
    Manual_weight = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.child_id
class auto(models.Model):
    child_id =  models.ForeignKey(child,on_delete = models.CASCADE, blank = True, null = True)
    Date = models.DateField(null=True)
    Auto_height = models.CharField(max_length=64, null=True)
    Auto_weight = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.child_id