from django.forms import ModelForm
from .models import Vehicle


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle', 'registration_number', 'chassis_number',
                  'tyre_size', 'tyre_quantity', 'remarks']
