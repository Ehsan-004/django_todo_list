from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField(default=False)
    start_date = models.DateField(default=now)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'Task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
