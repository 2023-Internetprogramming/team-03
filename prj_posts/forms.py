from django import forms
from .models import Prj

class PrjForm(forms.ModelForm):
    
    GRADE_CHOICES = [
        (1, '1학년'),
        (2, '2학년'),
        (3, '3학년'),
        (4, '4학년'),
    ]
    
    prj_membernum = forms.TypedChoiceField(
        label='모집 인원',
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')],
        coerce=int
    )
    
    user_grade = forms.ChoiceField(choices=GRADE_CHOICES, label='학년', initial=1, widget=forms.Select())

    class Meta:
        model = Prj
        exclude = ['author']
        fields = ["user_name", "user_major", 'prj_name',  "user_grade", "prj_membernum", "post_content"]

        labels = {
            'user_name' : '모집자',
            'user_major' : '전공',
            'user_grade' : '학년',
            'prj_name' : '프로젝트 이름',
            'prj_membernum' : '모집 인원',
            'post_content' : '내용',            
        }