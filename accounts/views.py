from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # Go to login after they sign up
    success_url = reverse_lazy('login')
    template_name='accounts/signup.html'