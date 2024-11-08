from django import forms
from . import models


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = models.Product
        fields = ['title', 'category', 'brand', 'description', 'serie_number', 'cost_price', 'selling_price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'serie_number': forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control', 'rows': 3}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'title': 'Fornecedor',
            'category': 'Produto',
            'brand': 'Quantidade',
            'description': 'Descrição',
            'serie_number': 'Numero de serie',
            'cost_price': 'Preço de custo',
            'selling_price': 'Preço de venda',
        }