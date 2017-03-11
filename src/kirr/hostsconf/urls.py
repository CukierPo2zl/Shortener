from django.conf.urls import url
from .views import wildcard_redirect


urlpatterns = [
    url(r'^(?P<path>.*)', wildcard_redirect),
]


'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<shortcode>[\w-]+)/$', kirr_redirect_view),
    url(r'^(?P<shortcode>[\w-]+)/$', KirrCBView.as_view()),
]
'''
