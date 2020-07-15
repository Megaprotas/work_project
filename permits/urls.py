from django.urls import path
from .views import PermitOpenListView, PermitClosedListView, GeneralPermitDetailView, HotWorksPermitDetailView, ElectricalWorksPermitDetailView, GeneralPermitCreateView, HotWorkslPermitCreateView, ElectricalWorkslPermitCreateView, GeneralEditView, HotWorksEditView, ElectricalEditView

urlpatterns = [
    path('permits/', PermitOpenListView.as_view(), name='permits_open'),
    path('permits/closed', PermitClosedListView.as_view(), name='permits_closed'),
    path('permits/general/<int:pk>/', GeneralPermitDetailView.as_view(), name='general_detail_view'),
    path('permits/hotworks/<int:pk>/', HotWorksPermitDetailView.as_view(), name='hotworks_detail_view'),
    path('permits/electrical/<int:pk>/', ElectricalWorksPermitDetailView.as_view(), name='electrical_detail_view'),
    path('permit/general_new/', GeneralPermitCreateView.as_view(), name='general_permit_create'),
    path('permit/hotworks_new/', HotWorkslPermitCreateView.as_view(), name='hotworks_permit_create'),
    path('permit/electrical_new/', ElectricalWorkslPermitCreateView.as_view(), name='electrical_permit_create'),
    path('permit/<int:pk>/general_edit/', GeneralEditView.as_view(), name='general_edit'),
    path('permit/<int:pk>/hotworks_edit/', HotWorksEditView.as_view(), name='hotworks_edit'),
    path('permit/<int:pk>/electrical_edit/', ElectricalEditView.as_view(), name='electrical_edit'),
]