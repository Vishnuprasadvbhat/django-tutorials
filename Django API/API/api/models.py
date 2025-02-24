from django.db import models

# Create your models here.


# ORM --> Object Relation mapping --> maps python object to database instance
# Higher Level python Wrapper 

# class Blog(models.Model):
#   Name = models.TextField(default='Default Name')
#   title = models.CharField(max_length=108)
#   content = models.TextField()
#   published_date = models.DateTimeField(auto_now_add=True)



class candidate(models.Model):
  first_name = models.CharField(max_length=100, default='Default Name')
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  phone = models.BigIntegerField()
  registered_date = models.DateTimeField(auto_now_add=True)


# id, first_name, last_name, email, phone, registered_date


def __str__(self):
  return self.title
