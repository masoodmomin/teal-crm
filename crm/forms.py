from .models import *
from django import forms
from django.forms import ModelForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets={
                   "name":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "phone":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "email":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "address":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                }  

class Form(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets={
                   "product":forms.Select(attrs={'class': "form-control form-control-sm"}),
                   "customer":forms.Select(attrs={'class': "form-control form-control-sm"}),
                   "status":forms.Select(attrs={'class': "form-control form-control-sm"}),
                }  


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets={
                   "name":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "product":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "vendor":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "discount":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                   "cost":forms.TextInput(attrs={'class': "form-control form-control-sm"}),
                } 