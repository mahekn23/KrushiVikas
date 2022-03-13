from django import forms
from .models import RentModel


class RentForm(forms.ModelForm):
    class Meta:
        model = RentModel
        fields = [
            "tool_name",
            "owner_name",
            "contact_number",
            "email_id",
            "tool_description",
            "rent_price",
            "image",
        ]
        widgets = {"user": forms.HiddenInput(), "uid": forms.HiddenInput()}
