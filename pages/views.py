from django.shortcuts import render
from .models import Contact
from django.views.generic import(

    CreateView,
    TemplateView
) 

# Create your views here.


class HomeView(TemplateView):
    template_name = "pages/index.html"

class ServiceView(TemplateView):
    template_name = "pages/services.html"

class ContactCreateView(CreateView):
    model =Contact
    fields =['name','email','comments']
    template_name="pages/contact.html"
    success_url="/"