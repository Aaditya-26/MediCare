import re
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, User


class CustomUserCreationForm(UserCreationForm):
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
            raise forms.ValidationError('Username can only contain letters, numbers, and @/./+/-/_ characters.')
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


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'phone_number', 'blood_group',
                  'featured_image', 'history', 'nid', 'dob', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError('Name is required.')
        if not re.match(r"^[A-Za-z\s\-']+$", name):
            raise forms.ValidationError('Name can only contain letters, spaces, hyphens, or apostrophes.')
        if len(name) < 2:
            raise forms.ValidationError('Name must be at least 2 characters.')
        if len(name) > 100:
            raise forms.ValidationError('Name cannot exceed 100 characters.')
        return name.title()

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
            raise forms.ValidationError('Age is required.')
        if age < 0 or age > 150:
            raise forms.ValidationError('Please enter a valid age (0–150).')
        return age

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone is None:
            return phone
        phone_str = str(phone)
        if len(phone_str) < 7 or len(phone_str) > 15:
            raise forms.ValidationError('Enter a valid phone number (7–15 digits).')
        return phone

    def clean_nid(self):
        nid = self.cleaned_data.get('nid', '').strip()
        if nid and len(nid) < 5:
            raise forms.ValidationError('NID must be at least 5 characters.')
        return nid


class PasswordResetForm(forms.Form):
    # Fix: was ModelForm(User) — form.save(commit=False) created a phantom unsaved
    # User object instead of looking up the existing one by email. The generated
    # token was for an object with pk=None so reset links always failed.
    # Now a plain Form; the view handles user lookup explicitly.
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control floating', 'placeholder': 'Enter your registered email'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if not re.match(r'^[\w\.\+\-]+@[\w\-]+\.[a-z]{2,}$', email):
            raise forms.ValidationError('Enter a valid email address.')
        # Validate user exists — view will handle silently if not found
        return email
