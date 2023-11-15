from django.db import models

class TeamMember(models.Model):
    position = models.CharField(max_length=50)
    skills = models.TextField()
    people = models.IntegerField()
    description_OTT = models.TextField()

    def __str__(self):
        return self.name
