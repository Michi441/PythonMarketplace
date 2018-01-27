"""sixerr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from sixerapp import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', views.home, name='home'),
    url(r'^gigs/(?P<id>[0-9]+)/$', views.gig_detail, name='gig_detail'),
    url('/social', include('social_django.urls', namespace='social')),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url('^auth/', include('django.contrib.auth.urls', namespace="auth")),
    url(r'^my_gigs/$', views.my_gigs, name='my_gigs'),
    url(r'^create_gig/$', views.create_gig, name='create_gig'),
    url(r'^edit_gig/(?P<id>[0-9]+)$', views.edit_gig, name='edit_gig'),
    url(r'^profile/(?P<username>\w+)/$', views.profile, name="profile"),
    url(r'^checkout/$', views.checkout, name="checkout"),
    url(r'^my_sellings/$', views.my_sellings, name="my_sellings"),
    url(r'^my_buys/$', views.my_buys, name='my_buys')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
