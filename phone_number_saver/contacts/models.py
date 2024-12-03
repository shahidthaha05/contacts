from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"


import re
from django.db import models

class PhoneNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="phone_numbers")
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def clean_phone_number(self):
        """Clean and format the phone number to be in the correct WhatsApp format"""
        # Remove any non-numeric characters (except +)
        cleaned_number = re.sub(r'[^0-9+]', '', self.number)
        return cleaned_number

    def save(self, *args, **kwargs):
        self.number = self.clean_phone_number()  # Clean number before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}: {self.number}"





  

    def save(self, *args, **kwargs):
        self.number = self.clean_phone_number()  # Clean number before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}: {self.number}"
