from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Permit(models.Model):
    profile = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    contractor = models.CharField(max_length=100, default='')
    contractor_name = models.CharField(max_length=100, default='')
    facility = models.CharField(max_length=100, default='')
    date_of_arrival = models.DateField(auto_now_add=False, default=timezone.now)
    time_of_arrival = models.TimeField(auto_now_add=False, default=timezone.now)
    date_of_finish = models.DateField(auto_now_add=False, default=timezone.now)
    time_of_finish = models.TimeField(auto_now_add=False, default=timezone.now)
    job_location = models.CharField(max_length=100, default='')
    job_spec = models.TextField(max_length=500, default='')
    equipment = models.TextField(max_length=100, default='')
    status_closed = models.BooleanField(default=False)
    works_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'%s %s on %s' % (self.contractor, self.contractor_name, self.date_of_arrival)


class General(Permit):
    safety_precautions = models.TextField(max_length=200, default='')
    ra_ready = models.BooleanField(default=False)
    ms_ready = models.BooleanField(default=False)
    confined_space_entry = models.BooleanField(default=False)

    def __str__(self):
        return f'%s from %s on %s' % (self.contractor_name, self.contractor, self.date_of_arrival)

    def get_absolute_url(self):
        return reverse('general_detail_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'General Permit'
        verbose_name_plural = 'General Permits'
        ordering = ('date_of_arrival', )


class HotWorks(Permit):
    ppe = models.BooleanField(default=False)
    welding_screen = models.BooleanField(default=False)
    smoke_heat_isolated = models.BooleanField(default=False)

    def __str__(self):
        return f'%s from %s on %s' % (self.contractor_name, self.contractor, self.date_of_arrival)

    def get_absolute_url(self):
        return reverse('hotworks_detail_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Hot Works Permit'
        verbose_name_plural = 'Hot Works Permits'
        ordering = ('date_of_arrival', )


class ElectricalWorks(Permit):
    location1 = models.CharField(max_length=100, default='')
    location2 = models.CharField(max_length=100, default='')
    location3 = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'%s from %s on %s' % (self.contractor_name, self.contractor, self.date_of_arrival)

    def get_absolute_url(self):
        return reverse('electrical_detail_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Electrical Works Permit'
        verbose_name_plural = 'Electrical Works Permits'
        ordering = ('date_of_arrival', )
