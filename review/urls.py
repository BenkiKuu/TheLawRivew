from django.conf import settings
# from django.conf.urls.static import static
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static



urlpatterns=[
    url(r'^$', views.home, name='index'),
    url(r'^profile/(?P<profile_id>\d+)$', views.profile, name='profile'),
    url(r'^new_profile/$', views.new_profile, name='new_profile'),
    url(r'^new_firm/$', views.new_firm, name='new_firm'),
    url(r'^new_demand/$', views.new_demand, name='new_demand'),
    url(r'^new_aff/$', views.new_aff, name='new_aff'),
    url(r'^new_demand_doc/$', views.demand_tmp, name='new_demand_temp'),
    url(r'^qrcodes$', views.qrcodes, name='qrcodes')


]
# (?P<profile_id>\d+)
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
