from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Contest(models.Model):
    
    CATEGORY_CHOICES = [
        ('기획/아이디어', '기획/아이디어'),
        ('광고/마케팅', '광고/마케팅'),
        ('사진/영상/UCC', '사진/영상/UCC'),
        ('디자인', '디자인'),
        ('예체능', '예체능'),
        ('IT/소프트웨어/게임', 'IT/소프트웨어/게임'),
    ]
    
    contest_title = models.CharField(max_length=30)
    contest_description = models.TextField()
    deadline = models.DateField()
    link = models.URLField()
    contest_image = models.ImageField(upload_to='contest/images/%Y/%m/%d/', blank=True)
    contest_view_count = models.IntegerField(default=0)
    contest_category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='기획/아이디어')
    scraped_by_users = models.ManyToManyField(User, related_name='scraped_contests', blank=True)
    
    def __str__(self):
        return self.contest_title

#댓글
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=100, default='Anonymous')
    comment = models.TextField(default='')
    contest_post = models.ForeignKey(Contest, on_delete=models.CASCADE, null=True, default=None)
    created_at = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.comment