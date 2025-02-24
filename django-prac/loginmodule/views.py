from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def login(request):
  return render(request, 'content/login.html')


def register(request):
  if request.method == 'POST':  
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    if password == confirm_password:

      user = User.objects.create_user(username, email, password)
      user.save()
      return render(request, 'login.html')
  
  else:
    return render(request, 'content/register.html')
  

def dashboard(request):
  if request == POST:
    pass