from django.forms import ModelForm
from .models import Vehicle


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle', 'registration_number', 'chassis_number',
                  'tyre_size', 'tyre_quantity', 'remarks']

    def clean_registration_number(self):
        value = self.cleaned_data["registration_number"]
        return value.strip().upper()

    def clean_chassis_number(self):
        value = self.cleaned_data["chassis_number"]
        return value.strip().upper()