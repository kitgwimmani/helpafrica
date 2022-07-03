from os import link
from turtle import position, title
from django.db import models


# Create your models here.

class Content (models.Model):
    CAT = (
        ('news', 'News'),
        ('event', 'Events'),
        ('gallery', 'Gallery'),
        ('support', 'Support')
    )
    category = models.CharField(
        choices=CAT,
        max_length=10
    )
    caption = models.CharField(max_length=40)
    body = models.TextField()
    posted_at = models.DateField()
    upload = models.ImageField(null=True, blank=True, upload_to ='uploads/')

    def __str__(self):
        return self.caption

#import data
from .choices import *
class Member(models.Model):
    fullname = models.CharField(max_length=64)
    home_address = models.TextField()
    residential_address = models.TextField()
    dob = models.DateField()
    blood_group = models.CharField(
        choices=BLOOD_GROUP,
        max_length=3
    )
    religion = models.CharField(
        choices=RELIGION,
        max_length=20
    ) 
    gender = models.CharField(
        choices=GENDER,
        max_length=6
    )
    state = models.CharField(
        choices=STATE,
        max_length=30
    )
    lga = models.CharField(max_length=40)
    polling_unit = models.CharField(max_length=40)
    ward = models.CharField(max_length=40)
    account_number = models.CharField(max_length=12)
    bank_name = models.CharField(
        choices=BANK,
        max_length=50
    )
    phone_number = models.CharField(max_length=15)
    whatapp_number = models.CharField(max_length=15)
    position = models.CharField(
        choices=POSITION,
        max_length=20
    )
    registration_number = models.CharField(max_length=15)
    signature = models.ImageField(null=True, blank=True, upload_to ='uploads/signature/')
    passport = models.ImageField(null=True, blank=True, upload_to ='uploads/passport/')

    def __str__(self):
        return self.fullname

class Support(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.title
    