from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^chaining/', include('smart_selects.urls')),
)
