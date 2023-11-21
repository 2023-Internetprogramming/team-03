from django import forms
from .models import Ott
from datetime import datetime

class OttForm(forms.ModelForm):
    class Meta:
        model = Ott
        fields = ['type', 'people', 'bill', 'description_OTT']
        
        labels = {
            'type': 'OTT 종류',
            'bill' : '총 결제 금액',
            'people' : '모집 인원',
            'description_OTT' : '상세 정보',      
        }

        widgets = {
            'type': forms.RadioSelect(choices=Ott.TYPE_CHOICES),
        }
