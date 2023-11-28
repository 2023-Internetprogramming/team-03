from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Study(models.Model):
    TYPE_CHOICES = [
        ('학업', '학업'),
        ('어학', '어학'),
        ('자격증', '자격증'),
        ('고시', '고시'),
        ('취업', '취업'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=15)
    user_name = models.CharField(max_length=5)
    user_major = models.CharField(max_length=15)
    user_grade = models.IntegerField(default=1)
    study_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default="학업")
    study_member = models.IntegerField(default=1)

    post_content = models.TextField()

    join_list = models.ManyToManyField(
        User,
        blank=True,
        related_name='study_user'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.post_title}'
    
    def get_absolute_url(self):
        return f'/study/{self.pk}/'