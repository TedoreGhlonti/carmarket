# accounts/views.py

from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUSerCreationForm

class SignUpView(CreateView):
    form_class = CustomUSerCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
