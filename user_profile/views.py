from django.shortcuts import render
# Create your views here.
from . forms import ProfileCreationForm
from django.views.generic import CreateView


class ProfileCreateView(CreateView):
    form_class = ProfileCreationForm
    template_name = 'user_profile/create.html'
