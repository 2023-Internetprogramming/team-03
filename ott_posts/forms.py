from django import forms
from .models import Ott
from datetime import datetime

class OttForm(forms.ModelForm):
    
    TYPE_CHOICES = [
        ('Netflix', 'Netflix'),
        ('Tving', 'Tving'),
        ('Disney+', 'Disney+'),
        ('Wave', 'Wave'),
        ('Coupangplay', 'Coupangplay')
    ]
    
    type = forms.ChoiceField(choices=TYPE_CHOICES, label='OTT 종류', widget=forms.Select(attrs={'onchange': 'updateBill()'}))
    people = forms.ChoiceField(
        choices=[(1, '1명'), (2, '2명'), (3, '3명'), (4, '4명')],
        label='모집 인원',
        widget=forms.Select(attrs={'onchange': 'updateBill()'})
    )
        
    class Meta:
        model = Ott
        exclude = ['author']
        fields = ['type', 'people', 'bill', 'description_OTT']
        
        labels = {
            'type': 'OTT 종류',
            'bill' : '총 결제 금액',
            'people' : '모집 인원',
            'description_OTT' : '상세 정보',      
        }
