from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)
from . models import CodeBank

# Create your views here.


class CodeBankDeleteView(DeleteView):
    queryset = CodeBank.objects.all()


class CodeBankCreateView(CreateView):
    template_name = 'codebank/create.html'
    queryset = CodeBank.objects.all()
    fields = '__all__'
    success_url = '../'


class CodeBankListView(ListView):
    template_name = 'codebank/list.html'
    queryset = CodeBank.objects.all()


class CodeBankUpdateView(UpdateView):
    model = CodeBank
    template_name = 'codebank/update.html'
    queryset = CodeBank.objects.all()
    fields = '__all__'
    success_url = '../'
