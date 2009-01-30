from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import *
from django.conf import settings
from django.template.loader import render_to_string
from django.db.models import get_model

from django_newsletter.models import Subscription
from django_newsletter.forms import SubscriptionForm
from django_newsletter.core import csv

import datetime
import re

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def generate_csv(request, model_str="django_newsletter.subscription"):
    '''
    TODO:
    
    '''
    model = get_model(*model_str.split('.')
    objs = model._default_manager.filter(subscribed=True)
    
    if len(objs) == 0:
        objs = [["no subscriptions"],]
    return csv.ExcelResponse(objs)

def subscribe_detail(request, form_class=SubscriptionForm, 
        template_name='newsletter/subscribe.html',  
        success_template='newsletter/success.html', extra_context={}, 
        model_str="django_newsletter.subscription"):
    
    '''
    TODO:
    '''
    
    if request.POST:   
        form = form_class(request.POST)
        
        if form.is_valid():
            
            subscribed = form.cleaned_data["subscribed"]
            email = form.cleaned_data["email"]
            subscription = None
            model = None
            try:
                """
                if the user already exists we're just gonna update
                otherwise the form, as is, will throw an exception
                if the unique email already exists.
                """
                
                model = get_model(*model_str.split('.')) 
                model._default_manager.get(email=email)    
                subscription.subscribed = subscribed
                subscription.save()
            except (AttributeError, model.DoesNotExist):
                #contiue on processing
                pass
            
            message = getattr(settings,
                "NEWSLETTER_OPTIN_MESSAGE", "Success! You've been added.")
            
            #if opt-out
            if not subscribed:
                message = getattr(settings,
                     "NEWSLETTER_OPTOUT_MESSAGE", 
                     "You've been removed. Sorry to see ya go.")          
            
            #ok so this is a new signup, save()
            if not subscription:
                form.save()

            extra = {
                'success': True,
                'message': message,
                'form': form_class(),
            }
            extra.update(extra_context)
            
            return render_to_response(success_template, extra, 
                 RequestContext(request))
    else:
        form = form_class()
    
    extra = {
        'form': form,
    }
    extra.update(extra_context)
    
    return render_to_response(template_name, extra, RequestContext(request))

