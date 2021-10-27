from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now=True)
    content=models.TextField(max_length=1024,blank=False,null=True)
    image=models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.content[:40]


class Friend(models.Model):
    person1=models.ForeignKey(User,on_delete=models.CASCADE,related_name="person1")
    person2=models.ForeignKey(User,on_delete=models.CASCADE,related_name="person2")

    def __str__(self):
        return self.person1.username +" - "+ self.person2.username

