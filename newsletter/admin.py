from django.contrib import admin
from django_newsletter.models import Subscription
from django_newsletter.forms import SubscriptionForm

class SubscriptionAdmin(admin.ModelAdmin):
    
    list_display = ('email', 'subscribed', 'created_on', )
    search_fields = ('email',)
    list_filter = ('subscribed',)
    
admin.site.register(Subscription, SubscriptionAdmin)
