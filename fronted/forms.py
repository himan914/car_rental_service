from django import forms 
from .models import *

class Booking_form(forms.ModelForm):

	
    cname = forms.CharField()
    email = forms.EmailField()
    ph_no = forms.CharField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    Address = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Booking
        fields=['cname','email','ph_no','start_date','end_date','Address']
