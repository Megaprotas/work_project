from django.urls import path
from .views import CalloutListView, CalloutDetailView, CalloutCreateView, CalloutDeleteView, CalloutEditView, IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('callout/', CalloutListView.as_view(), name='callout'),
    path('callout/<int:pk>/', CalloutDetailView.as_view(), name='callout_detail'),
    path('callout/new/', CalloutCreateView.as_view(), name='callout_create'),
    path('callout/<int:pk>/edit/', CalloutEditView.as_view(), name='callout_edit'),
    path('callout/<int:pk>/delete/', CalloutDeleteView.as_view(), name='callout_confirm_delete'),
]