from django.db import models

class Registration(models.Model):
    email = models.CharField(max_length=400)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_agreed_coc = models.BooleanField()
    registration_date = models.DateTimeField("date registered")
