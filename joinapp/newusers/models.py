from unittest import result
from django.db import models

class NewUser(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=75)
    terms_of_service = models.BooleanField(default=False, blank=True, null=True)
    
    def __str__(self):
        result = '{0.name} {0.email} {0.username} {0.password} {0.terms_of_service} '
        return result.format(self)
        

