from django.contrib import admin
from newsletter.models import Subscription
from newsletter.forms import SubscriptionForm

class SubscriptionAdmin(admin.ModelAdmin):
    
    list_display = ('email', 'subscribed', 'created_on', )
    search_fields = ('email',)
    list_filter = ('subscribed',)
    
admin.site.register(Subscription, SubscriptionAdmin)
