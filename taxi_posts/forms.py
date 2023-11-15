from django import forms
from .models import Ride
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['departure_location', 'destination', 'departure_time', 'available_seats', 'description']
        labels = {
            'departure_location': _('출발지'),
            'destination': _('목적지'),
            'departure_time' : _('출발 시간'),
            'available_seats' : _('모집 인원'),
            'description' : _('상세 정보'),
        }
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(RideForm, self).__init__(*args, **kwargs)
        self.initial['departure_time'] = datetime.now().strftime('%Y-%m-%dT%H:%M')

        # error_message = {
        #     'name' : {
        #         'max_length': _("제목이 너무 길어요")
        #     }
        # }
    