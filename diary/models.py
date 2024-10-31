from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Memo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:  # If the object is being created
            self.created_at = timezone.localtime(timezone.now())

        # Ensure modified_at is updated only on modification
        self.modified_at = timezone.localtime(timezone.now())

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title