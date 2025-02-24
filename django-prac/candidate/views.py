# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# from django.contrib.auth import authenticate, login, logout 



# def register(request):
#   if request.method == 'POST':
#     form = UserCreationForm(request.POST)

#     if form.is_valid():
#       user = form.save()
#       login(request, user)
#       return redirect('home') #redirect to home page
#   else:
#     form = UserCreationForm()
    
#   return render(request, 'content/register.html', {'form': form}) 


# def login(request):
#   if request.method == "POST":
#     username = request.POST['username']
#     password = request.POST['password']
#     user =  authenticate(request, username = username, password = password)
#     if user is not None:
#       login(request,user)
#       return redirect('home') #redirect to home page
#   return render(request, 'content/login.html')

# def logout(request):
#   logout(request)
#   return redirect('home')


# def user_home(request):
#   return render(request, 'content/home.html')

# def candidatelogin(request):
#   return render(request,'content/candidate.html')


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # redirect to home page
    else:
        form = UserCreationForm()
    
    return render(request, 'content/register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # redirect to home page
        else:
            # Add an error message if authentication fails
            return render(request, 'content/login.html', {'error': 'Invalid username or password'})
    return render(request, 'content/login.html')

def user_logout(request):
    auth_logout(request)
    return redirect('home')

def user_home(request):
    return render(request, 'content/home.html')

def candidate_login(request):
    return render(request,'content/candidate.html')
