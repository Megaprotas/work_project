from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

form_styles = {
            'first_name': forms.TextInput(attrs={'class': 'textinputfield'}),
            'username': forms.TextInput(attrs={'class': 'textinputfield'}),
            'surname': forms.TextInput(attrs={'class': 'textinputfield'}),
            'position': forms.TextInput(attrs={'class': 'textinputfield'}),
            'email': forms.EmailInput(attrs={'class': 'textinputfield'}),
            'password1': forms.PasswordInput(attrs={'class': 'textinputfield'}),
            'password2': forms.PasswordInput(attrs={'class': 'textinputfield'}),
          }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = form_styles

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'User Name'
        self.fields['email'].label = 'E-mail'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Repeat Password'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = form_styles

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'User Name'
        self.fields['email'].label = 'E-mail'


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'surname', 'position']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Name'
        self.fields['surname'].label = 'Family Name'
        self.fields['position'].label = 'Position'
