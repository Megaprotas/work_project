from django.contrib import admin
from .models import Permit, General, HotWorks, ElectricalWorks

admin.site.register(Permit)
admin.site.register(General)
admin.site.register(HotWorks)
admin.site.register(ElectricalWorks)
