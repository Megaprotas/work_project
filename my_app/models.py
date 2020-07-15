from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Callout(models.Model):
    BWD = 'BWD'
    CCH = 'CCH'
    HND = 'HND'
    SYO = 'SYO'
    FACILITY = (
        (BWD, 'BWD'),
        (CCH, 'CCH'),
        (HND, 'HND'),
        (SYO, 'SYO')
    )

    C1 = 'C1'
    C2 = 'C2'
    C3 = 'C3'
    PRIORITY = (
        (C1, 'C1'),
        (C2, 'C2'),
        (C3, 'C3')
    )

    ELECTRICAL = 'electrical'
    LEAK = 'leak'
    ALARM = 'alarm'
    MEDICAL_GAS = 'medical_gas'
    DRAINAGE_BLOCK = 'drainage_block'
    TEMP_ISSUES = 'temp_issues'
    WEAR_TEAR = 'wear_tear'
    FAULT_CAUSE = (
        (ELECTRICAL, 'electrical'),
        (LEAK, 'leak'),
        (ALARM, 'alarm'),
        (MEDICAL_GAS, 'medical_gas'),
        (DRAINAGE_BLOCK, 'drainage_block'),
        (TEMP_ISSUES, 'temp_issues'),
        (WEAR_TEAR, 'wear_tear')
    )

    engineer = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='')
    facility = models.CharField(max_length=20, choices=FACILITY, default=BWD)
    callout_date = models.DateField(auto_now_add=False, default=timezone.now)
    notification_time = models.TimeField(auto_now_add=False, default=timezone.now)
    arrival_time = models.TimeField(auto_now_add=False, default=timezone.now)
    completion_time = models.TimeField(auto_now_add=False, default=timezone.now)
    mileage = models.DecimalField(default=0.0, max_digits=6, decimal_places=2)
    ref_number = models.PositiveIntegerField(default=0)
    findings = models.TextField(max_length=500)
    actions_taken = models.TextField(max_length=500)
    resolved_status = models.BooleanField()
    follow_up_status = models.BooleanField()
    support_required_status = models.BooleanField()
    priority_status = models.CharField(max_length=5, choices=PRIORITY, default=C1)
    fault_case = models.CharField(max_length=20, choices=FAULT_CAUSE, default=C1)
    published_date = models.DateField(default=timezone.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'%s to %s' % (self.notification_time, self.facility)

    def get_absolute_url(self):
        return reverse('callout_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Callout'
        verbose_name_plural = 'Callouts'
        ordering = ('callout_date', )
