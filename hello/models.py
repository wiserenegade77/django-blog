from django.db import models

# Create your models here.
class About(models.Model):
    email=models.CharField(max_length=122)
    email2=models.CharField(max_length=122)

    def __str__(self):
        return self.email