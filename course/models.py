from django.db import models

class Course(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    is_free = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
