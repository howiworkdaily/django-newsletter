from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import datetime

class SubscriptionBase(models.Model):
    '''
    A newsletter subscription base.
    
    '''

    subscribed = models.BooleanField(_('subscribed'), default=True)
    email = models.EmailField(_('email'), unique=True)
    created_on = models.DateField(_("created on"), blank=True)
    updated_on = models.DateField(_("updated on"), blank=True)
    
    class Meta:
        abstract = True
    
    @classmethod
    def is_subscribed(cls, email):
        '''
        Concept inspired by Satchmo. Thanks guys!
        
        '''
        try:
            return cls.objects.get(email=email).subscribed
        except cls.DoestNotExist, e:
            return False
         
    
    def __unicode__(self):
        return u'%s' % (self.email)
        
    def save(self, *args, **kwargs):
        self.updated_on = datetime.date.today()
        if not self.created_on:
            self.created_on = datetime.date.today()
        super(SubscriptionBase,self).save(*args, **kwargs)

class Subscription(SubscriptionBase):
    '''
    Generic subscription
    
    '''
        
    def save(self, *args, **kwargs):
        super(Subscription,self).save()
