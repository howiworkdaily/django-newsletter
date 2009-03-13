from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',

    (r'^newsletter/', include('newsletter.urls')), 
    (r'^admin/(.*)', admin.site.root),
    url (
        r'^$',
        direct_to_template,
        {'template': 'home.html'},
        name = 'home',
        ),
)

urlpatterns += patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)


