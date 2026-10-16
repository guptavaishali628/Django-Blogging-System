# step-1-->first import user model

from django.contrib.auth.models import User 
# import UserCreationForm
from django.contrib.auth.forms import UserCreationForm

# step 2-> create class
# this registrationform will extend the functionality of the user creation form:

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('email', 'username', 'password1', 'password2')


