from django.db import models

# Create your models here.

class adress(models.Model):
    addr_zipcode = models.CharField(max_length=255)
    addr_street = models.CharField(max_length=255)
    addr_number = models.CharField(max_length=255)
    addr_complement = models.CharField(max_length=255, blank=True)
    addr_district  = models.CharField(max_length=255)
    addr_city = models.CharField(max_length=255)
    addr_state = models.CharField(max_length=255)
    addr_country = models.CharField(max_length=255, default='Brasil')





class userAdd(models.Model):
    user_name = models.CharField(max_length=255)
    user_lastname = models.CharField(max_length=255)
    user_document = models.CharField(max_length=255, unique=True)    
    user_phone = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)
    user_registration = models.DateTimeField(auto_now_add=True)
    address = models.OneToOneField(adress, on_delete=models.CASCADE, default=None)


class companyAdd(models.Model):
    company_name = models.CharField(max_length=255)
    company_fantasy_name = models.CharField(max_length=255)
    company_document = models.CharField(max_length=255, unique=True)    
    company_phone = models.CharField(max_length=255)
    company_email = models.EmailField(max_length=255)
    company_registration = models.DateTimeField(auto_now_add=True)
    address = models.OneToOneField(adress, on_delete=models.CASCADE, default=None)


    
    