from django.db import models

class User(models.Model):   # or User if that's the actual model
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)   # <-- added this
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # password = models.CharField(max_length=20, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
