from django.db import models

# Create your models here.
class Book(models.Model):

  class Meta: app_label = 'library'

  title = models.CharField()
  author = models.CharField()
  publication_date = models.DateField()
  description= models.TextField()
  price = models.DecimalField(max_digits=5, decimal_places=2)
  pages = models.IntegerField()



  def __str__(self):
    return self.title