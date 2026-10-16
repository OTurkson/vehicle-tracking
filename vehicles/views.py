from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.core.paginator import Paginator

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
    # Read search query and optional tyre_size filter from GET parameters
    search_query = request.GET.get("q", "").strip()
    tyre_size_filter = request.GET.get("tyre_size", "").strip()

    # Start with all vehicles
    vehicles = Vehicle.objects.all()

    # Apply search query if provided
    if search_query:
        vehicles = vehicles.filter(
            Q(vehicle__icontains=search_query) |
            Q(registration_number__icontains=search_query) |
            Q(chassis_number__icontains=search_query) |
            Q(tyre_size__icontains=search_query) |
            Q(remarks__icontains=search_query)
        )

    # Apply tyre size filter if provided
    # if tyre_size_filter:
    #     vehicles = vehicles.filter(tyre_size=tyre_size_filter)
        
    # Keep order consistent by ordering by vehicle name and registration number
    vehicles = vehicles.order_by("vehicle", "registration_number")

    # Paginate the results to show 10 vehicles per page
    paginator = Paginator(vehicles, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

     # Populate the filter with sizes that actually exist.
    # tyre_sizes = (
    #     Vehicle.objects
    #     .exclude(tyre_size="")
    #     .order_by("tyre_size")
    #     .values_list("tyre_size", flat=True)
    #     .distinct()
    # )

    context = {
        "page_obj": page_obj,
        "query": search_query,
        "selected_tyre_size": tyre_size_filter,
        # "tyre_sizes": tyre_sizes,
    }

    if request.headers.get("HX-Request") == "true":
        return render(
            request,
            "vehicles/partials/_vehicle_results.html",
            context,
        )

    return render(request, "vehicles/index.html", context)


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
    