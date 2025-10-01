from django import forms
from .models import Comment

# Create class to handle user input for recommending posts by email (name, email, to, comments)
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    pass

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']