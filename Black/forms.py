from django import forms
from .models import MyUser
from .admin import UserCreationForm


class RegForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=["email","phonenumber","First_name","Last_name","Bio","password1","password2"]

    def clean(self):
            # pass
            cleaned_data = super().clean()
            password = cleaned_data.get("password")
            confirmpassword = cleaned_data.get("confirmpassword")
            if password != confirmpassword:
                msg = "password mismatch"
                self.add_error("password", msg)


class LoginForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)
