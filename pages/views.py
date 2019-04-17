from django.shortcuts import render
from .models import Contact
from django.core.mail import EmailMessage
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

    def form_valid(self, form):
        response = super(ContactCreateView, self).form_valid(form)
        str_body = "Hi " + form.instance.name + \
            ", <p> Thanks for contacting us.</p><br/> We have received your request. We'll connect with you shortly.<p>Regards, <br/>Biome Consulting</p>"

        msg = EmailMessage(
            'Free Quote Request',
            str_body,
            'info@biome.consulting',
            [form.instance.email]
        )
        msg.content_subtype = 'html'
        msg.send()
        str_body = form.instance.comments + '<br/> email: ' + \
            form.instance.email + '<br/> name: ' + form.instance.name
        msg = EmailMessage(
            'Free Quote Request',
            str_body,
            'info@biome.consulting',
            ['bhanu.net10@gmail.com', 'vba.libraries@gmail.com', 'info@biome.consulting']
        )
        msg.content_subtype = 'html'
        msg.send()
        # send_mail(
        #     'Free Quote Request',
        #     html_message=str_body,
        #     'info@biome.consulting',
        #     [form.instance.email],
        #     fail_silently=False

        # )
        return response

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data(**kwargs)
        context['contact_page'] = 'active'
        return context
