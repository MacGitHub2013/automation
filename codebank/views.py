from django.shortcuts import render
from django.shortcuts import reverse
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

    def get_success_url(self):
        return reverse('codebank:list')

    def get(self, *args, **kwargs):
        return self.post(*args, *kwargs)

    # def get_success_url(self):
    #     return reverse('codebank:list')


class CodeBankCreateView(CreateView):
    template_name = 'codebank/create.html'
    queryset = CodeBank.objects.all()
    fields = '__all__'
    success_url = '../'


class CodeBankListView(ListView):
    template_name = 'codebank/list.html'
    queryset = CodeBank.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CodeBankListView, self).get_context_data(**kwargs)
        context['code_bank'] = 'active'
        return context


class CodeBankUpdateView(UpdateView):
    model = CodeBank
    template_name = 'codebank/update.html'
    queryset = CodeBank.objects.all()
    fields = '__all__'
    success_url = '../'
