from django.shortcuts import render
from .models import Contact
from django.views.generic import(

    CreateView,
    TemplateView
)

# Create your views here.


class AboutView(TemplateView):

    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about_page'] = 'active'
        return context


class HomeView(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['home_page'] = 'active'
        return context


class ServiceView(TemplateView):
    template_name = "pages/services.html"

    def get_context_data(self, **kwargs):
        context = super(ServiceView, self).get_context_data(**kwargs)
        context['service_page'] = 'active'
        return context


class ContactCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'comments']
    template_name = "pages/contact.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data(**kwargs)
        context['contact_page'] = 'active'
        return context
