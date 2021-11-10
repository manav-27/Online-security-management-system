from django.db import models
from django.contrib.auth.models import User
# Create your models here.
Roles = (
    ('manager', 'MANAGER'),
    ('guard', 'GUARD'),
)
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=None, null=True)
    role = models.CharField(max_length=50,choices=Roles, default='guard')

class Guard(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=None, null=True)
    AllowedHolidays=models.IntegerField(default=4)
    requestst=models.IntegerField(default=0)
    requestdone=models.CharField(default=0,max_length=10,null=True)
    requestmsg=models.CharField(default=None,max_length=500,null=True)
    date=models.CharField(default=None,max_length=15,null=True)
    manno=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.user.username


class TT(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=None, null=True)
    mon =models.CharField(default=None,max_length=500)
    tue =models.CharField(default=None,max_length=500)
    wed =models.CharField(default=None,max_length=500)
    thu =models.CharField(default=None,max_length=500)
    fri =models.CharField(default=None,max_length=500)
    sat =models.CharField(default=None,max_length=500)
    sun =models.CharField(default=None,max_length=500)

    def __str__(self):
        return self.user.username


