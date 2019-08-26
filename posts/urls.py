from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_a_post

urlpatterns = [
    # Root directory for the posts app
    url(r'^$', get_posts, name='get_posts'),
    # Get post by its ID
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    # Create a new post - same function as edit but different name
    url(r'^new/$', create_or_edit_a_post, name='new_post'),
    # Edit post - get post by its ID
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_a_post, name='edit_post'),
]