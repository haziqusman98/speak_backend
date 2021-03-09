from django.db import models
from django.core.exceptions import FieldDoesNotExist

class Sign(models.Model):
    character = models.CharField(max_length=1)
    image = models.URLField(max_length=200)
    
    def __str__(self):
        return f'{self.character}'
