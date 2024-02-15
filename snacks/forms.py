from django import forms
from .models import Snack

class SnackCreateForm(forms.ModelForm):
    purchase_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Snack
        fields = ['title', 'purchaser', 'description', 'reviewer', 'purchase_date']
