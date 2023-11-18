from django.db import models

class Contest(models.Model):
    contest_title = models.CharField(max_length=30)
    contest_description = models.TextField()
    deadline = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.title
