from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید'}), label='نام کاربری')
    password = forms.CharField(max_length = 32, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'}), label='رمز عبور')

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید'}), label="نام کاربری")
    email = forms.EmailField(max_length = 50 ,widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}), label="ایمیل")
    password = forms.CharField(max_length = 32, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'}), label='رمز عبور')
    confirmpassword = forms.CharField(max_length = 32, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را مجددا وارد کنید'}), label='تایید رمز عبور')