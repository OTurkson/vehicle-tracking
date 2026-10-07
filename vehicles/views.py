from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import VehicleForm

# Create your views here.
@login_required
def index(request):
    return render(request, "index.html")

@login_required
def create_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = VehicleForm()
    return render(request, "create.html", {"form": form})