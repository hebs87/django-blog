from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):
    class Meta:
        # Use the Post model that we created in models.py
        model = Post
        # Only want editable fields visible
        fields = ('title', 'content', 'image', 'tag', 'published_date')
        
