from django import forms
from .models import Study

class StudyForm(forms.ModelForm):

    class Meta:
        model = Study
        fields = ["user_name", "user_major", "user_grade", "study_type", "study_membernum", "post_content"]

        labels = {
            'user_name' : '모집자',
            'user_major' : '전공',
            'user_grade' : '학년',
            'study_type' : '스터디 종류',
            'study_membernum' : '모집 인원',
            'post_content' : '내용',            
        }