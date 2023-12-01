from django import forms
from .models import Prj
from contest.models import Contest


class PrjForm(forms.ModelForm):
    
    GRADE_CHOICES = [
        (1, '1학년'),
        (2, '2학년'),
        (3, '3학년'),
        (4, '4학년'),
    ]
    
    prj_member = forms.TypedChoiceField(
        label='모집 인원',
        choices=[(1, '1명'), (2, '2명'), (3, '3명'), (4, '4명'), (5, '5명'), (6, '6명'), (7, '7명'), (8, '8명'), (9, '9명'), (10, '10명')],
        coerce=int
    )
    
    MAJOR_CHOICES = [
        ('컴퓨터공학전공', '컴퓨터공학전공'),
        ('디지털소프트웨어공학부', '디지털소프트웨어공학부'),
        ('IT미디어공학전공', 'IT미디어공학전공'),
        ('소프트웨어전공', '소프트웨어전공'),
        ('사이버보안전공', '사이버보안전공'),
        ('바이오공학전공', '바이오공학전공'),
        ('정보통계학전공', '정보통계학전공'),
        ('식품영양학전공', '식품영양학전공'),
        ('수학전공', '수학전공'),
        ('화학전공', '화학전공'),
        ('약학과', '약학과'),
        ('경영학전공', '경영학전공'),
        ('문헌정보학전공', '문헌정보학전공'),
        ('유아교육과', '유아교육과'),
        ('문화인류학전공', '문화인류학전공'),
        ('회계학전공', '회계학전공'),
        ('심리학전공', '심리학전공'),
        ('국제통상학전공', '국제통상학전공'),
        ('법학전공', '법학전공'),
        ('사회학전공', '사회학전공'),
        ('아동가족학전공', '아동가족학전공'),
        ('사회복지학전공', '사회복지학전공'),
        ('정치외교학전공', '정치외교학전공'),
        ('국어국문학전공', '국어국문학전공'),
        ('일어일문학전공', '일어일문학전공'),
        ('중어중문학전공', '중어중문학전공'),
        ('영어영문학전공', '영어영문학전공'),
        ('불어불문학전공', '불어불문학전공'),
        ('독어독문학전공', '독어독문학전공'),
        ('스페인어전공', '스페인어전공'),
        ('사학전공', '사학전공'),
        ('철학전공', '철학전공'),
        ('미술사학전공', '미술사학전공'),
        ('의상디자인전공', '의상디자인전공'),
        ('철학전공', '철학전공'),
        ('철학전공', '철학전공'),
    ]
    
    user_grade = forms.ChoiceField(choices=GRADE_CHOICES, label='학년', initial=1, widget=forms.Select())
    user_major = forms.ChoiceField(choices=MAJOR_CHOICES, label='전공', widget=forms.Select())
    
    contest = forms.ModelChoiceField(
        queryset=Contest.objects.all(),
        required=False,
        label='공모전 선택',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    
    prj_name = forms.CharField(
        required=False,
        label='프로젝트 이름',
        help_text='공모전을 선택하거나 프로젝트 이름을 입력해야 합니다.',
    )
    
    def clean(self):
        cleaned_data = super().clean()
        contest = cleaned_data.get("contest")
        prj_name = cleaned_data.get("prj_name")

        if not contest and not prj_name:
            raise forms.ValidationError("공모전을 선택하거나 프로젝트 이름을 입력해야 합니다.")

    class Meta:
        model = Prj
        exclude = ['author']
        fields = ["user_major", "contest", 'prj_name',  "user_grade", "prj_member", "post_content"]

        labels = {
            'user_major' : '전공',
            'user_grade' : '학년',
            'prj_member' : '모집 인원',
            'post_content' : '내용',      
        }