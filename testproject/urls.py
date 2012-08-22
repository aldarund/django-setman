from django.conf import settings
from django.conf.urls.defaults import include, patterns
from django.contrib import admin
from django.contrib.auth.decorators import login_required

try:
    from django.views.generic.simple import direct_to_template
except ImportError:
    from django.views.generic import TemplateView
    home_view = TemplateView.as_view(template_name='home.html')
    home_data = {}
else:
    home_view = direct_to_template
    home_data = {'template': 'home.html'}


admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', login_required(home_view), home_data, 'home'),

    (r'^odesk_auth/', include('django_odesk.auth.urls')),

    (r'^accounts/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'registration/logout.html'}),
    (r'^accounts/', include('django.contrib.auth.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^setman/', include('setman.urls')),
    (r'^test/', include('testproject.core.urls')),
)

if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('django.views.static',
        ('^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), 'serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
