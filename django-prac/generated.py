import os
import django
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'careerhub.settings') 
django.setup()

print("DJANGO_SETTINGS_MODULE:", os.environ.get('DJANGO_SETTINGS_MODULE'))


user = User.objects.get(username='Vishnuprasad')  # Replace with the correct username
token, created = Token.objects.get_or_create(user=user)
print(f"Token for {user.username}: {token.key}")

'''
Username (leave blank to use 'vishn'): Vishnuprasad
Email address: vishnuprasadvbhat@gmail.com
Password: 
Password (again): 

Token for Vishnuprasad: 2d05956a73d4913559fb6ab941f8fa8c06181b7f

Creating unit tests for your custom serializers and views?
Pagination, filtering, or search for your API?
Deploying your API to a production server?
Now that you have the token generation process clear, let me know if you want to:

Secure your custom UI with token-based authentication using this token.
Move to unit testing for your views and serializers.
Implement pagination and search in your API.
'''



# exec(open('generated.py').read())
