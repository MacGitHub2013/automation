from django.urls import path
from . views import(
    HomeView,
    ServiceView,
    ContactCreateView,
    AboutView
)

app_name = "pages"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('services/', ServiceView.as_view(), name='services'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about')
]
