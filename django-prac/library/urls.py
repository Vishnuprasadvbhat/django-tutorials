from django.urls import path
from . import views

urlpatterns = [
  # path('', views.home, name= 'homepage'),
  path('books/', views.BookListView.as_view(), name= 'homepage'),
  path('books/<int:pk>/', views.BookDetailView.as_view() , name= 'homepage'),
  path('', views.home, name= 'homepage'),

]