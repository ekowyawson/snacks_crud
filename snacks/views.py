from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack
from .forms import SnackCreateForm  # Import the custom form

class HomeView(TemplateView):
  template_name = 'home.html'

class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack
  context_object_name = 'snacks'

class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack

class SnackCreateView(CreateView):
    model = Snack
    form_class = SnackCreateForm  # Use the custom form
    # fields = ['title', 'purchaser', 'description', 'reviewer', 'purchase_date']
    template_name = 'snack_create.html'
    success_url = reverse_lazy('snack_list')

class SnackUpdateView(UpdateView):
    model = Snack
    fields = ['title', 'purchaser', 'description', 'reviewer', 'purchase_date']
    template_name = 'snack_update.html'
    success_url = reverse_lazy('snack_list')

class SnackDeleteView(DeleteView):
    model = Snack
    success_url = reverse_lazy('snack_list')  # Redirects to the snack list after deletion
    template_name = 'snack_confirm_delete.html'  # Optional: If you want a separate confirmation page
