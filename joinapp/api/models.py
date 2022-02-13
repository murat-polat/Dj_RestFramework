from django.db import models

class NewUser(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=75)
    terms_of_service = models.BooleanField()
    
    def __str__(self):
        return(self.name, self.username,
        self.email, self.password, self.terms_of_service)

