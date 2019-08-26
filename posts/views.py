# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


# Create your views here.
def get_posts(request):
    '''
    Creat a view that will return a list of Posts that were published
    prior to 'now' and render them to the 'blogposts.html template
    '''
    # Filter all posts on published date that is less than/equal to
    # timezone now, and order by the published date in descending order
    posts = Post.objects.filter(published_date__lte=timezone.now())\
                                .order_by('-published_date')
    # Render the HTML template, which returns the list of posts
    return render(request, 'blogposts.html', {'posts': posts})


def post_detail(request, pk):
    '''
    Create a view that returns a single Post object based on the
    post ID (pk) and rendet it to the 'postdetail.html' template.
    Or return a 404 error if the post is not found
    '''
    # Get Post by ID (pk)
    post = get_object_or_404(Post, pk=pk)
    # Increment views by 1
    post.views += 1
    # Save post and render HTML and send back our post object
    post.save()
    return render(request, 'postdetail.html', {'post': post})


def create_or_edit_a_post(request, pk=None):
    '''
    Create a view that allows us to create or edit a post depending if
    the Post ID is null or not
    '''
    # Get the object if there is an ID, or set ID to None if new post
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == 'POST':
        # If as a result of posting the form, we want to get details
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # If form is valid, redirect to post_detail form using Post ID
            post = form.save()
            return redirect(post_detail, post.pk)
    # If method isn't POST, just return the form with instance=post
    else:
        form = BlogPostForm(instance=post)
    # Return form when page initially loads
    return render(request, 'blogpostform.html', {'form': form})
