from django.db import models

# Create your models here.
class Community(models.Model):
    name = models.TextField()
    description = models.TextField()
    updates = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name