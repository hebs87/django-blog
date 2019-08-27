"""blog URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
# Allows to redirect to a view
from django.views.generic import RedirectView
from django.views.static import serve
# Import MEDIA_ROOT from settings.py to enable to serve out our media URL
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Root directory - redirect to posts directory
    url(r'^$', RedirectView.as_view(url='posts/')),
    # Want posts to pass using URLs in urls.py file in posts directory
    url(r'posts/', include('posts.urls')),
    # Point media towards path towards particular file
    # Use servce library to serve up document root, which is MEDIA_ROOT
    url(r'^media/(?<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
