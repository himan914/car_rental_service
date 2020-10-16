"""car_rent URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from fronted.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view(),name='home'),
    url(r'^search_query/$',search),
    url(r'car/(\d+)/$',CarDetail,name='detail'),
    url(r'^contactus/$',contactus,name="contactus"),

    
    url(r'book/(?P<car>\d+)/$',BookingDetail.as_view(),name='listinfo'),
    url(r'^booking/(\d+)/$',NewBooking,name="book"),
    url(r'^logout/$',logout),
    url(r'^logged_in/',loggedin),
    url(r'^invalid/$',invalid_login),
    url(r'^register/$',register_user,name="register"),
    url(r'^register_success/$',register_success),
    url(r'^nextpage/$',nextpage,name="nextpage"),
    url(r'^login/$',login,name="log"),

    

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
