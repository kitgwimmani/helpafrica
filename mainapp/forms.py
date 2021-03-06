from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Member

#create form
class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ('fullname','home_address','residential_address','date_of_birth','blood_group', 'religion','gender','state','lga','account_number', 'bank_name','phone_number','whatapp_number','position','registration_number','signature','passport')

    