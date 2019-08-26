# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Import timezone as we are working with a date and time
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    '''
    A single Blog post
    '''
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Date and time populated as soon as record created (auto_now_add)
    created_date = models.DateTimeField(auto_now_add=True)
    # Starts off blank, nulls allowed and default value is that time
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    views = models.IntegerField(default=0)
    # Tags to group by - starts off blank and nulls allowed
    tag = models.CharField(max_length=30, blank=True, null=True)
    # Image field and upload to the img directory in media
    image = models.ImageField(upload_to="img", blank=True, null=True)


    # Optional but good practise to have it
    def __unicode__(self):
        return self.title
