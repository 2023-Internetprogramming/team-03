from django import forms
from .models import Prj

class PrjForm(forms.ModelForm):

    class Meta:
        model = Prj
        fields = ["post_title", "user_name", "user_major",  "user_grade", "prj_membernum", "post_content"]

        labels = {
            'post_title' : '제목',
            'user_name' : '모집자',
            'user_major' : '전공',
            'user_grade' : '학년',
            'prj_membernum' : '모집 인원수',
            'post_content' : '내용',            
        }