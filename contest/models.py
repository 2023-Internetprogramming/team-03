from django.db import models

class Contest(models.Model):
    contest_title = models.CharField(max_length=30)
    contest_description = models.TextField()
    deadline = models.DateField()
    link = models.URLField()
    contest_image = models.ImageField(upload_to='contest/images/%Y/%m/%d/', blank=True)
    contest_view_count = models.IntegerField(default=0)

#댓글
class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contest_title
