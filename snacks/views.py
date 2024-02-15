from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from .models import Snack

class HomeView(TemplateView):
  template_name = 'home.html'

class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack
  context_object_name = 'snacks'

class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack

# def index(request):
#     return HttpResponse("Hello, world. You're at the snacks index.")