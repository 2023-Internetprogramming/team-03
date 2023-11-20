from django.db import models

class Contest(models.Model):
    
    CATEGORY_CHOICES = [
        ('기획/아이디어', '기획/아이디어'),
        ('광고/마케팅', '광고/마케팅'),
        ('사진/영상/UCC', '사진/영상/UCC'),
        ('디자인', '디자인'),
        ('예체능', '예체능'),
        ('문학/시나리오', '문학/시나리오'),
        ('IT/소프트웨어/게임', 'IT/소프트웨어/게임'),
    ]
    
    contest_title = models.CharField(max_length=30)
    contest_description = models.TextField()
    deadline = models.DateField()
    link = models.URLField()
    contest_image = models.ImageField(upload_to='contest/images/%Y/%m/%d/', blank=True)
    contest_view_count = models.IntegerField(default=0)
    contest_category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)

#댓글
class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contest_title
