from re import T
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    # a user can have multiple tasks
    # on_delete: what to do when a user is deleted? Cascade: remove the task
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank = True)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["complete"]

