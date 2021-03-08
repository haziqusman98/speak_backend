from django.db import models

class Sign(models.Model):
    character = models.CharField(max_length=1)
    image = models.URLField(max_length=200)
    
    def __str__(self):
        return f'{self.character}'
