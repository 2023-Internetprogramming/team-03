from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from contest.models import Contest


class Prj(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=15)
    user_name = models.CharField(max_length=5)
    user_major = models.CharField(max_length=15)
    user_grade = models.IntegerField(default=1)
    prj_name = models.CharField(max_length=15, blank=True)
    prj_membernum = models.IntegerField(default=1)
    post_content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    contest = models.ForeignKey(Contest, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.post_title}'
    
    def get_absolute_url(self):
        return f'/prj/{self.pk}/'
    