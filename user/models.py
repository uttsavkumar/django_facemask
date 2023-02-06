from django.db import models
from django.contrib.auth.models import User
# Create your models here.

Gender = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
)

class Accounts(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(choices=Gender,max_length=10)
    dp = models.ImageField(upload_to='dp/', height_field=None, width_field=None, max_length=None,null=True)
    def __str__(self):
        return self.contact

        
class Post(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    caption = models.CharField(null=True,max_length=100)
    description = models.TextField(null=True)
    createAt = models.DateTimeField(auto_now_add=True)  
    image = models.ImageField( upload_to='post/', height_field=None, width_field=None, max_length=None,null=True)