# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post


# Register your models here.
# Register Post class with the admin site so it is accessible from there
admin.site.register(Post)
