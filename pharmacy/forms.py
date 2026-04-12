import re
from django.forms import ModelForm
from django import forms
from .models import Medicine, Cart


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'weight', 'quantity', 'featured_image',
                  'medicine_category', 'price', 'stock_quantity', 'Prescription_reqiuired']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs['placeholder'] = 'e.g. Paracetamol 500mg'
        self.fields['weight'].widget.attrs['placeholder'] = 'e.g. 500mg'
        self.fields['price'].widget.attrs['placeholder'] = 'Price in BDT'
        self.fields['stock_quantity'].widget.attrs['placeholder'] = 'Available units'

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError('Medicine name is required.')
        if len(name) < 2:
            raise forms.ValidationError('Medicine name must be at least 2 characters.')
        if len(name) > 200:
            raise forms.ValidationError('Medicine name cannot exceed 200 characters.')
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise forms.ValidationError('Price is required.')
        if price < 0:
            raise forms.ValidationError('Price cannot be negative.')
        if price > 1000000:
            raise forms.ValidationError('Please enter a realistic price.')
        return price

    def clean_stock_quantity(self):
        stock = self.cleaned_data.get('stock_quantity')
        if stock is None:
            return stock
        if stock < 0:
            raise forms.ValidationError('Stock quantity cannot be negative.')
        if stock > 100000:
            raise forms.ValidationError('Stock quantity seems unrealistically high.')
        return stock

    def clean_quantity(self):
        qty = self.cleaned_data.get('quantity')
        if qty is not None and qty < 0:
            raise forms.ValidationError('Quantity cannot be negative.')
        return qty


class CartUpdateForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update({'class': 'form-control', 'min': '1'})

    def clean_quantity(self):
        qty = self.cleaned_data.get('quantity')
        if qty is None or qty < 1:
            raise forms.ValidationError('Quantity must be at least 1.')
        if qty > 999:
            raise forms.ValidationError('Quantity cannot exceed 999.')
        return qty
