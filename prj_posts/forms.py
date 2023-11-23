from django import forms
from .models import Prj

class PrjForm(forms.ModelForm):

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