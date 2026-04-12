import re
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from hospital.models import User, Hospital_Information
from .models import Admin_Information, Clinical_Laboratory_Technician


def _validate_user_creation(form_instance):
    """Shared validation for all staff user creation forms."""
    pass


class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if len(username) < 3:
            raise forms.ValidationError('Username must be at least 3 characters.')
        if len(username) > 30:
            raise forms.ValidationError('Username cannot exceed 30 characters.')
        if not re.match(r'^[\w.@+-]+$', username):
            raise forms.ValidationError('Username may only contain letters, numbers, and @/./+/-/_ characters.')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
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


class LabWorkerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if len(username) < 3:
            raise forms.ValidationError('Username must be at least 3 characters.')
        if len(username) > 30:
            raise forms.ValidationError('Username cannot exceed 30 characters.')
        if not re.match(r'^[\w.@+-]+$', username):
            raise forms.ValidationError('Username may only contain letters, numbers, and @/./+/-/_ characters.')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
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


class PharmacistCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if len(username) < 3:
            raise forms.ValidationError('Username must be at least 3 characters.')
        if len(username) > 30:
            raise forms.ValidationError('Username cannot exceed 30 characters.')
        if not re.match(r'^[\w.@+-]+$', username):
            raise forms.ValidationError('Username may only contain letters, numbers, and @/./+/-/_ characters.')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
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


class AddHospitalForm(ModelForm):
    class Meta:
        model = Hospital_Information
        fields = ['name', 'address', 'featured_image', 'phone_number', 'email', 'hospital_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError('Hospital name is required.')
        if len(name) < 3:
            raise forms.ValidationError('Hospital name must be at least 3 characters.')
        if len(name) > 200:
            raise forms.ValidationError('Hospital name cannot exceed 200 characters.')
        return name

    def clean_address(self):
        address = self.cleaned_data.get('address', '').strip()
        if not address:
            raise forms.ValidationError('Address is required.')
        if len(address) < 5:
            raise forms.ValidationError('Please enter a valid address.')
        return address

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone is None:
            raise forms.ValidationError('Phone number is required.')
        phone_str = str(phone)
        if len(phone_str) < 7 or len(phone_str) > 15:
            raise forms.ValidationError('Enter a valid phone number (7–15 digits).')
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if email and not re.match(r'^[\w\.\+\-]+@[\w\-]+\.[a-z]{2,}$', email):
            raise forms.ValidationError('Enter a valid email address.')
        return email


class EditHospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital_Information
        fields = ['name', 'address', 'featured_image', 'phone_number', 'email', 'hospital_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError('Hospital name is required.')
        if len(name) < 3:
            raise forms.ValidationError('Hospital name must be at least 3 characters.')
        return name

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone is not None:
            phone_str = str(phone)
            if len(phone_str) < 7 or len(phone_str) > 15:
                raise forms.ValidationError('Enter a valid phone number (7–15 digits).')
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if email and not re.match(r'^[\w\.\+\-]+@[\w\-]+\.[a-z]{2,}$', email):
            raise forms.ValidationError('Enter a valid email address.')
        return email


class EditEmergencyForm(forms.ModelForm):
    class Meta:
        model = Hospital_Information
        fields = ['general_bed_no', 'available_icu_no', 'regular_cabin_no', 'emergency_cabin_no', 'vip_cabin_no']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def _clean_bed_count(self, field_name, label):
        value = self.cleaned_data.get(field_name)
        if value is not None:
            if value < 0:
                raise forms.ValidationError(f'{label} cannot be negative.')
            if value > 10000:
                raise forms.ValidationError(f'{label} seems unrealistically high.')
        return value

    def clean_general_bed_no(self):
        return self._clean_bed_count('general_bed_no', 'General bed count')

    def clean_available_icu_no(self):
        return self._clean_bed_count('available_icu_no', 'ICU count')

    def clean_regular_cabin_no(self):
        return self._clean_bed_count('regular_cabin_no', 'Regular cabin count')

    def clean_emergency_cabin_no(self):
        return self._clean_bed_count('emergency_cabin_no', 'Emergency cabin count')

    def clean_vip_cabin_no(self):
        return self._clean_bed_count('vip_cabin_no', 'VIP cabin count')


class AddEmergencyForm(ModelForm):
    class Meta:
        model = Hospital_Information
        fields = ['name', 'general_bed_no', 'available_icu_no', 'regular_cabin_no', 'emergency_cabin_no', 'vip_cabin_no']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class AdminForm(ModelForm):
    class Meta:
        model = Admin_Information
        fields = ['name', 'email', 'phone_number', 'role', 'featured_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError('Name is required.')
        if not re.match(r"^[A-Za-z\s\.\-']+$", name):
            raise forms.ValidationError('Name can only contain letters, spaces, dots, or hyphens.')
        if len(name) < 2:
            raise forms.ValidationError('Name must be at least 2 characters.')
        return name.title()

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if email and not re.match(r'^[\w\.\+\-]+@[\w\-]+\.[a-z]{2,}$', email):
            raise forms.ValidationError('Enter a valid email address.')
        return email

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone is not None:
            phone_str = str(phone)
            if len(phone_str) < 7 or len(phone_str) > 15:
                raise forms.ValidationError('Enter a valid phone number (7–15 digits).')
        return phone
