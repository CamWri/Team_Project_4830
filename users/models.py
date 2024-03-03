from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length = 255)
    lastName = models.CharField(max_length = 255)
    email = models.CharField(null = True, max_length = 300)
    phone = models.IntegerField(null = True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"