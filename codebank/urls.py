from django.urls import path
from .views import (
    CodeBankCreateView,
    CodeBankListView,
    CodeBankUpdateView,
    CodeBankDeleteView
)
app_name = 'codebank'
urlpatterns = [
    path('add/', CodeBankCreateView.as_view(), name='create'),
    path('', CodeBankListView.as_view(), name='list'),
    path('<int:pk>/update', CodeBankUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', CodeBankDeleteView.as_view(), name='delete')
]
