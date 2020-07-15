from django import forms
from .models import Callout
from django.contrib.auth.models import User


class CalloutForm(forms.ModelForm):

    class Meta:
        model = Callout
        exclude = ('engineer', 'published_date', 'views', )

        widgets = {
            'callout_date': forms.DateInput(attrs={'class': 'textinputfield'}),
            'notification_time': forms.TimeInput(attrs={'class': 'textinputfield'}),
            'arrival_time': forms.TimeInput(attrs={'class': 'textinputfield'}),
            'completion_time': forms.TimeInput(attrs={'class': 'textinputfield'}),
            'mileage': forms.NumberInput(attrs={'class': 'textinputfield'}),
            'ref_number': forms.NumberInput(attrs={'class': 'textinputfield'}),
            'findings': forms.Textarea(attrs={'class': 'textareafield',
                                              'placeholder': 'Please specify findings'}),
            'actions_taken': forms.Textarea(attrs={'class': 'textareafield',
                                                    'placeholder': 'Please specify actions'})
        }

    def clean(self):
        super(CalloutForm, self).clean()
        findings = self.cleaned_data.get('findings')
        actions_taken = self.cleaned_data.get('actions_taken')
        mileage = self.cleaned_data.get('mileage')

        error1 = ['Minimum 10 characters required']
        error2 = ['You will not be compensated for fuel if mileage is 0']

        if len(findings) < 10:
            self._errors['findings'] = self.error_class(error1)
        if len(actions_taken) < 10:
            self._errors['actions_taken'] = self.error_class(error1)

        if mileage <= 0:
            self._errors['mileage'] = self.error_class(error2)

    def __init__(self, *args, **kwargs):
        super(CalloutForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Requester\' Name'
        self.fields['facility'].label = 'Facility/Hospital'

        self.fields['ref_number'].required = False
