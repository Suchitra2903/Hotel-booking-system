"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from hotel import settings
from hotelmanagement import views as user_views
from hoteladmin import views as admin_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', user_views.index, name="index"),
    url(r'^user_register/$' , user_views.register, name="register"),
    url(r'^user_home/$' , user_views.home, name="home"),
    url(r'^user_viewdetails/$' , user_views.viewdetails, name="viewdetails"),
    url(r'^user_singlewithac/$', user_views.singlewithac, name="singlewithac"),
    url(r'^user_singlewithoutac/$',user_views.singlewithoutac, name="singlewithoutac"),
    url(r'^user_doublewithac/$',user_views.singlewithoutac, name="doublewithac"),
    url(r'^user_doublewithoutac/$',user_views.singlewithoutac, name="doublewithoutac"),
    url('^userrequest/(?P<pk>\d+)/', user_views.userrequest, name="userrequest"),
    url('^user_mydetails/$', user_views.mydetails, name="mydetails"),
    url('^logout/$', user_views.logout, name="logout"),





    url(r'^admin/adminlogin/$',admin_views.adminpage, name="adminpage"),
    url(r'^admin/uploadpage/$',admin_views.uploadpage, name="uploadpage"),
    url(r'^admin/viewuserrequest/$',admin_views.viewuserrequest, name="viewuserrequest"),
    url(r'^admin/userrequest/accept/(?P<pk>\d+)/$', admin_views.accept, name="accept"),
    url(r'^admin/userrequest/reject/(?P<pk>\d+)/$', admin_views.reject, name="reject"),
    url('^logout/$', admin_views.adlogout, name="adlogout"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)