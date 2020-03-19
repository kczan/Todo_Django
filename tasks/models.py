from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=35)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.title
