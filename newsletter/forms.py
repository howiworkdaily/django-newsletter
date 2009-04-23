from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from newsletter.models import Subscription

class SubscriptionForm(forms.ModelForm):
    '''
    TODO:
    
    '''

    class Meta:
        model = Subscription


        
        
        
