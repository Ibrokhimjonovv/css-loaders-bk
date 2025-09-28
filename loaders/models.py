from django.db import models

class Loader(models.Model):
    group_id = models.CharField(max_length=200, db_index=True)
    css = models.TextField()
    is_light = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.group_id} ({self.pk})"
