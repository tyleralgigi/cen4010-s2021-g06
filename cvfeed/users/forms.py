from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if email and not email.endswith('@fau.edu'):
            self.add_error('email', 'Please register with an @fau.edu email address!')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )