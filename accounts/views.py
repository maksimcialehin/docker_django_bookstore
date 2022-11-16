from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name: str = 'registration/signup.html'
