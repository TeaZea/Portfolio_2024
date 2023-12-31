from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    quick_description = models.TextField(default="quick description")
    technology = models.CharField(max_length=20)

    def __str__(self):
        return self.title