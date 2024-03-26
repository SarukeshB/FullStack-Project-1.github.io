from django.db import models

class Task(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=255)
    due_date = models.DateField()

    def __str__(self):
        return self.title
