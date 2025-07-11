from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UploadedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file', 'is_advertisement']
        labels = {
            'file': 'فایل',
            'is_advertisement': 'آیا این یک تبلیغ برای ادمین است؟'
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='ایمیل')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UsernameEmailAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='ایمیل', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'
        self.fields['password'].label = 'رمز عبور'

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if username and email:
            try:
                user = User.objects.get(username=username)
                if user.email != email:
                    raise forms.ValidationError("ایمیل وارد شده با نام کاربری مطابقت ندارد.")
            except User.DoesNotExist:
                raise forms.ValidationError("نام کاربری یافت نشد.")
        return cleaned_data