
from django import urls
from django.urls import path
from . import views 

urlpatterns = [
  # path('blogposts/', views.BlogView.as_view(), name='blogpost-view'),
  # path('update/<int:pk>', views.GetPostDelete.as_view(), name = "update"),
  path('candidate/<int:id>', views.fillcandidate.as_view(), name='blogpost-view'),

]