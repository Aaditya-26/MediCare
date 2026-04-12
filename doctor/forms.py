import re
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from hospital.models import User
from .models import Doctor_Information


class DoctorUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control floating'})

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if len(username) < 3:
            raise forms.ValidationError('Username must be at least 3 characters.')
        if len(username) > 30:
            raise forms.ValidationError('Username cannot exceed 30 characters.')
        if not re.match(r'^[\w.@+-]+$', username):
            raise forms.ValidationError('Username may only contain letters, numbers, and @/./+/-/_ characters.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if not email:
            raise forms.ValidationError('Email is required.')
        if not re.match(r'^[\w\.\+\-]+@[\w\-]+\.[a-z]{2,}$', email):
            raise forms.ValidationError('Enter a valid email address.')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('An account with this email already exists.')
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1', '')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters.')
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError('Password must contain at least one uppercase letter.')
        if not re.search(r'[a-z]', password):
            raise forms.ValidationError('Password must contain at least one lowercase letter.')
        if not re.search(r'\d', password):
            raise forms.ValidationError('Password must contain at least one number.')
        return password


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor_Information
        fields = ['name', 'email', 'phone_number', 'degree', 'department',
                  'featured_image', 'visiting_hour', 'consultation_fee',
                  'report_fee', 'dob', 'hospital_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError('Doctor name is required.')
        if not re.match(r"^[A-Za-z\s\.\-']+$", name):
            raise forms.ValidationError('Name can only contain letters, spaces, dots, or hyphens.')
        if len(name) < 3:
            raise forms.ValidationError('Name must be at least 3 characters.')
        return name.title()

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if email and not re.match(r'^[\w\.\+\-]+@[\w\-]+\.[a-z]{2,}$', email):
            raise forms.ValidationError('Enter a valid email address.')
        return email

    def clean_consultation_fee(self):
        fee = self.cleaned_data.get('consultation_fee')
        if fee is not None and fee < 0:
            raise forms.ValidationError('Consultation fee cannot be negative.')
        return fee

    def clean_report_fee(self):
        fee = self.cleaned_data.get('report_fee')
        if fee is not None and fee < 0:
            raise forms.ValidationError('Report fee cannot be negative.')
        return fee
