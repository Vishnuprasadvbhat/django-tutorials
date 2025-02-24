from django.db import models

# Create your models here.

class User(models.Model):
  username = models.CharField()
  first_name = models.CharField()
  last_name= models.CharField()
  email = models.EmailField()
  password = models.CharField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)



  
  def __str__(self):
    return self.username