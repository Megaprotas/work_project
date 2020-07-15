from django import forms
from .models import General, HotWorks, ElectricalWorks


form_styles = {'contractor': forms.TextInput(attrs={'class': 'textinputfield'}),
               'contractor_name': forms.TextInput(attrs={'class': 'textinputfield'}),
               'facility': forms.TextInput(attrs={'class': 'textinputfield'}),
               'date_of_arrival': forms.DateInput(attrs={'class': 'textinputfield'}),
               'time_of_arrival': forms.TimeInput(attrs={'class': 'textinputfield'}),
               'date_of_finish': forms.DateInput(attrs={'class': 'textinputfield'}),
               'time_of_finish': forms.TimeInput(attrs={'class': 'textinputfield'}),
               'job_location': forms.TextInput(attrs={'class': 'textinputfield'}),
               'job_spec': forms.TextInput(attrs={'class': 'textinputfield'}),
               'equipment': forms.TextInput(attrs={'class': 'textinputfield'}),
               'safety_precautions': forms.TextInput(attrs={'class': 'textinputfield'}),
               'location1': forms.TextInput(attrs={'class': 'textinputfield'}),
               'location2': forms.TextInput(attrs={'class': 'textinputfield'}),
               'location3': forms.TextInput(attrs={'class': 'textinputfield'}),
               }

field_order_list = ('contractor', 'contractor_name', 'facility', 'date_of_arrival',
                    'time_of_arrival', 'date_of_finish', 'time_of_finish', 'job_location', 'job_spec', 'equipment',)

general_field_list = ('safety_precautions', 'ra_ready', 'ms_ready', 'confined_space_entry')
hotworks_field_list = ('ppe', 'welding_screen', 'smoke_heat_isolated')
electrical_field_list = ('location1', 'location2', 'location3')


class GeneralForm(forms.ModelForm):

    class Meta:
        model = General
        exclude = ('profile', )
        widgets = form_styles

    field_order = ['status_closed', 'works_completed', field_order_list, general_field_list]

    def __init__(self, *args, **kwargs):
        super(GeneralForm, self).__init__(*args, **kwargs)
        self.fields['date_of_finish'].label = 'Date of Completion'
        self.fields['time_of_finish'].label = 'Time of Completion'
        self.fields['ra_ready'].label = 'Risk Assessment Ready'
        self.fields['ms_ready'].label = 'Method Statement Ready'


class HotWorksForm(forms.ModelForm):

    class Meta:
        model = HotWorks
        exclude = ('profile', )
        widgets = form_styles

    field_order = ['status_closed', 'works_completed', field_order_list, hotworks_field_list]

    def __init__(self, *args, **kwargs):
        super(HotWorksForm, self).__init__(*args, **kwargs)
        self.fields['date_of_finish'].label = 'Date of Completion'
        self.fields['time_of_finish'].label = 'Time of Completion'
        self.fields['ppe'].label = 'PPE ready'
        self.fields['welding_screen'].label = 'Welding Screen Required'
        self.fields['smoke_heat_isolated'].label = 'Smoke/Heat Detectors Isolated'


class ElectricalWorksForm(forms.ModelForm):

    class Meta:
        model = ElectricalWorks
        exclude = ('profile', )
        widgets = form_styles

    field_order = ['status_closed', 'works_completed', field_order_list, electrical_field_list]

    def __init__(self, *args, **kwargs):
        super(ElectricalWorksForm, self).__init__(*args, **kwargs)
        self.fields['date_of_finish'].label = 'Date of Completion'
        self.fields['time_of_finish'].label = 'Time of Completion'
        self.fields['location1'].label = 'Location 1'
        self.fields['location2'].label = 'Location 2'
        self.fields['location3'].label = 'Location 3'