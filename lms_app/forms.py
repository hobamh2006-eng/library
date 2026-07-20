from django import forms
from .models import Books,Category

class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'




class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


