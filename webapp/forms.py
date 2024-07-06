from django import forms
from django.forms import widgets

from webapp.models import GuestBook

class GuestForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label="name")
    email = forms.CharField(
        max_length=200,
        required=True,
        label="email",
        widget=forms.EmailInput(attrs={'class': 'forms-group__input'})
    )
    guest_note = forms.CharField(
        max_length=3000,
        required=True,
        label="guest note",
        widget=widgets.Textarea(attrs={"cols": 20, "rows": 5, "placeholder": "guest note"}),
    )



