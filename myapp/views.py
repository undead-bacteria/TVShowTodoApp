from django.views import generic
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import TelevisionShow
from .forms import TelevisionShowForm


class ShowListView(generic.ListView):
  model = TelevisionShow
  template_name = 'show_list.html'
  context_object_name = 'shows'
  paginate_by = 10

  def get_queryset(self):
    return TelevisionShow.objects.all().order_by('-release_date')


class ShowDetailView(generic.DetailView):
  model = TelevisionShow
  template_name = 'show_detail.html'
  context_object_name = 'show'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['related_shows'] = TelevisionShow.objects.filter(genre=self.object.genre)[:5]
    return context


class ShowCreateView(generic.CreateView):
  model = TelevisionShow
  form_class = TelevisionShowForm
  template_name = 'show_form.html'
  success_url = '/'
  
  def get_success_url(self):
    return reverse_lazy('show_detail', kwargs={'pk': self.object.pk})


class ShowUpdateView(generic.UpdateView):
  model = TelevisionShow
  form_class = TelevisionShowForm
  template_name = 'show_form.html'
  success_url = '/'

  def get_success_url(self):
    return reverse_lazy('show_detail', kwargs={'pk': self.object.pk})


class ShowDeleteView(generic.DeleteView):
  model = TelevisionShow
  template_name = 'show_confirm_delete.html'
  context_object_name = 'show'
  
  def get_success_url(self):
    return reverse_lazy('show_list')
  
  def form_valid(self, form):
    response = super().form_valid(form)
    if self.request.htmx:
      return JsonResponse({'redirect': self.get_success_url()})
    return response