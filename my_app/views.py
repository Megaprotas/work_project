from django.shortcuts import render
from .models import Callout
from .forms import CalloutForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone


class IndexPageView(TemplateView):
    template_name = 'index.html'


class CalloutListView(ListView):
    model = Callout
    template_name = 'callout.html'
    paginate_by = 10
    queryset = Callout.objects.all()

    def get_queryset(self):
        return Callout.objects.filter(published_date__lte=timezone.now()).order_by('-name')


class CalloutDetailView(DetailView):
    model = Callout
    template_name = 'callout_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        object = self.get_object()
        object.views += 1
        object.save()
        return context


class CalloutCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Callout
    form_class = CalloutForm
    success_message = "Instance was created successfully"
    template_name = 'callout_form.html'
    redirect_field_name = 'callout_detail.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.engineer = self.request.user
        self.object.save()
        return super().form_valid(form)


class CalloutEditView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Callout
    form_class = CalloutForm
    success_message = "Instance was updated successfully"
    template_name = 'callout_form.html'
    redirect_field_name = 'callout_detail.html'

    def get_queryset(self):
        return super(CalloutEditView, self).filter(profile=self.request.user)


class CalloutDeleteView(LoginRequiredMixin, DeleteView):
    model = Callout
    success_message = "Permanently removed"
    template_name = 'callout_confirm_delete.html'
    success_url = reverse_lazy('callout')

