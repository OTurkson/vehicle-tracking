from django.forms import ModelForm, TextInput, NumberInput, Textarea
from .models import Vehicle

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle

        fields = [
            "vehicle",
            "registration_number",
            "chassis_number",
            "tyre_size",
            "tyre_quantity",
            "remarks",
        ]

        widgets = {
            "vehicle": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Toyota Hilux",
                }
            ),
            "registration_number": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. GR-1234-24",
                }
            ),
            "chassis_number": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter chassis number",
                }
            ),
            "tyre_size": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. 265/65 R17",
                }
            ),
            "tyre_quantity": NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "1",
                    "placeholder": "e.g. 4",
                }
            ),
            "remarks": Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Optional remarks",
                }
            ),
        }

    # def clean_registration_number(self):
    #     value = self.cleaned_data["registration_number"]
    #     return value.strip().upper()

    # def clean_chassis_number(self):
    #     value = self.cleaned_data["chassis_number"]
    #     return value.strip().upper()