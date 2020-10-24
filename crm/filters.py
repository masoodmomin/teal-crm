import django_filters
from .models import Product
from django import forms

class ProductFilter(django_filters.FilterSet):
    name = django_filters.ModelChoiceFilter(queryset = Product.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    date_created = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'class': 'datepicker col form-control form-control-sm', 'placeholder': 'YYYY-MM-DD'}))    
    class Meta:
        model = Product
        fields = ['name','date_created']