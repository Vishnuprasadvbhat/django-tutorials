from django.shortcuts import render
from rest_framework import generics
from .models import candidate
from .serializer import   CandidateSerializer
from rest_framework.response import Response
# Generics contain generic views

# class BlogView(generics.ListCreateAPIView):
#   # specify the query set
#   queryset = Blog.objects.all() # Gives all instances of Blog Class

#   # specify the serializer 
#   serializer_class = BlogSerializer


# class GetPostDelete(generics.RetrieveUpdateDestroyAPIView):
#   queryset = Blog.objects.all()
#   serializer_class = BlogSerializer
  
# 


class fillcandidate(generics.ListAPIView):
  def get_data(self, request, id = None):
    if id:
      queryset = candidate.objects.get(id=id)
      serializer_class = CandidateSerializer(queryset)
      return Response(serializer_class.data)

    else:
      queryset = candidate.objects.all()
      serializer_class = CandidateSerializer(queryset, many=True)
      return Response(serializer_class.data)
