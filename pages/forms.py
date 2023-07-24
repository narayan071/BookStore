from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from book.models import Book


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        model = User

class AddBookform(ModelForm):
    class Meta:
        fields = "__all__"
        model = Book