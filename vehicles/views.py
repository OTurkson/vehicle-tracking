from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST

from vehicles.models import Vehicle

from .forms import VehicleForm

# Create your views here.

# default page - lists vehicles and provides options to create or delete vehicles
@login_required
@permission_required(
    "vehicles.view_vehicle",
    raise_exception=True
)
def index(request):
    vehicles = Vehicle.objects.all()
    return render(request, "vehicles/index.html", {"vehicles": vehicles})


# create a new vehicle
@login_required
@permission_required(
    "vehicles.add_vehicle",
    raise_exception=True
)
def create_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Vehicle created successfully.")

            return redirect("vehicles:index")
    else:
        form = VehicleForm()
    return render(request, "vehicles/form.html", {"form": form})


# edit/update a vehicle
@login_required
@permission_required(
    "vehicles.change_vehicle",
    raise_exception=True
)
def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()

            vehicle_name = f"{vehicle.vehicle} ({vehicle.registration_number})"
            messages.success(request, f"{vehicle_name} updated successfully.")

            return redirect("vehicles:index")
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, "vehicles/form.html", {"form": form, "vehicle": vehicle})


# delete a vehicle
@login_required
@permission_required('vehicles.delete_vehicle', raise_exception=True)
@require_POST
def delete_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    vehicle_name = f"{vehicle.vehicle} ({vehicle.registration_number})"
    
    vehicle.delete()
    
    messages.success(request, f"{vehicle_name} deleted successfully.")
    
    return redirect("vehicles:index")
    