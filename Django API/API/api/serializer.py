
# This takes the data and converts into JSON compatible .

from rest_framework import serializers
from .models import candidate


# class BlogSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Blog
#     fields = ['id', 'Name' ,'title', 'content', 'published_date']
    


class CandidateSerializer(serializers.ModelSerializer):
  class Meta:
    model = candidate
    # fields = '__all__'
    fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'registered_date']
