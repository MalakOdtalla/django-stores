from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Store
from django.urls import reverse_lazy


# Create your views here.

class Home(TemplateView):
    template_name = 'Home.html'

class StoresListView(ListView):
    template_name = 'Store_list.html'
    model = Store

class StoresDetailView(DetailView):
    template_name = 'stores\Store_detail.html'
    model = Store

class StoresCreateView(CreateView):
    template_name = 'stores\Store_create.html'
    model = Store
    fields = ['name', 'description', 'owner']

class StoresUpdateView(UpdateView):
    template_name = 'stores\Store_update.html'
    model = Store
    fields = ['name', 'description', 'owner']

class StoresDeleteView(DeleteView):
    template_name = 'stores\Store_delete.html'
    model = Store
    success_url = reverse_lazy('Store_list')