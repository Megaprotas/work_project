from django.shortcuts import render, HttpResponse
from .models import Permit, General, HotWorks, ElectricalWorks
from .forms import GeneralForm, HotWorksForm, ElectricalWorksForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone


new_success_message = "Instance was created successfully"


#List Views of all permits
class PermitOpenListView(ListView):
    template_name = 'permit.html'
    paginate_by = 20
    queryset = Permit.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PermitOpenListView, self).get_context_data(**kwargs)
        context['general'] = General.objects.filter(status_closed=False)
        context['hotworks'] = HotWorks.objects.filter(status_closed=False)
        context['electrical'] = ElectricalWorks.objects.filter(status_closed=False)
        return context


class PermitClosedListView(ListView):
    template_name = 'permit.html'
    paginate_by = 20
    queryset = Permit.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PermitClosedListView, self).get_context_data(**kwargs)
        context['general'] = General.objects.filter(status_closed=True)
        context['hotworks'] = HotWorks.objects.filter(status_closed=True)
        context['electrical'] = ElectricalWorks.objects.filter(status_closed=True)
        return context


#Permit detail Views
class GeneralPermitDetailView(DetailView):
    model = General
    template_name = 'general_detail_view.html'

    def generate_pdf(self):
        from reportlab.pdfgen import canvas
        response = HttpResponse(content_type='pdf')
        response['Content-Disposition'] = 'attachment; filename="permit.pdf"'
        p = canvas.Canvas(response)
        p.drawString(100, 100, "Company Name")
        p.showPage()
        p.save()
        print(p)
        return response

    def get(self, request, *args, **kwargs):
        if self.request.GET.get('zip', None):
            return self.generate_pdf()
        return super(GeneralPermitDetailView, self).get(request, *args, **kwargs)


class HotWorksPermitDetailView(DetailView):
    model = HotWorks
    template_name = 'general_detail_view.html'


class ElectricalWorksPermitDetailView(DetailView):
    model = ElectricalWorks
    template_name = 'general_detail_view.html'


#Create Views
class GeneralPermitCreateView(CreateView):
    login_url = 'login'
    model = General
    form_class = GeneralForm
    success_message = new_success_message
    template_name = 'create_form.html'
    redirect_field_name = 'general_detail_view.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.profile = self.request.user
        self.object.save()
        return super().form_valid(form)


class HotWorkslPermitCreateView(CreateView):
    login_url = 'login'
    model = HotWorks
    form_class = HotWorksForm
    success_message = new_success_message
    template_name = 'create_form.html'
    redirect_field_name = 'general_detail_view.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.profile = self.request.user
        self.object.save()
        return super().form_valid(form)


class ElectricalWorkslPermitCreateView(CreateView):
    login_url = 'login'
    model = ElectricalWorks
    form_class = ElectricalWorksForm
    success_message = new_success_message
    template_name = 'create_form.html'
    redirect_field_name = 'general_detail_view.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.profile = self.request.user
        self.object.save()
        return super().form_valid(form)


#Update Views
class GeneralEditView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = General
    form_class = GeneralForm
    success_message = "Instance was updated successfully"
    template_name = 'create_form.html'
    redirect_field_name = 'general_detail_view.html'


class HotWorksEditView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = HotWorks
    form_class = HotWorksForm
    success_message = "Instance was updated successfully"
    template_name = 'create_form.html'
    redirect_field_name = 'hotworks_detail_view.html'


class ElectricalEditView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = ElectricalWorks
    form_class = ElectricalWorksForm
    success_message = "Instance was updated successfully"
    template_name = 'create_form.html'
    redirect_field_name = 'electrical_detail_view.html'