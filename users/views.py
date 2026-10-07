from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

# Create your views here.

class LoginView(auth_views.LoginView):
    template_name = "users/login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("vehicles:index")

        return super().dispatch(request, *args, **kwargs)