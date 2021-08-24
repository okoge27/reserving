from typing import ClassVar
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Reserve, Log


class ReserveForm(ModelForm):
    class Meta:
        model = Reserve
        fields = ('customer_name','reserve_date', 'contents')
        

class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = ('reserve', 'text')


class UpdateLogForm(ModelForm):
    class Meta:
        model = Log
        fields = ('text',)


"""
class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class LoginForm(AuthenticationForm):
    def __init__(self, *args, kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
"""

