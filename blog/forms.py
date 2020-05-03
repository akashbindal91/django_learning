from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta(object):
        model = Post
        fields = ('auther', 'title', 'text')

        widgets = {
            """
                # class types used below :  
                default django class : editable, medium-editor-textarea
                our own custom class : textinputclass , postcontent
            """

            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            # class : refer again. text area is somewhat pre defined. its connected to css class.
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('auther', 'text')

        widgets = {
            """
                # class types used below :  
                default django class : editable, medium-editor-textarea
                our own custom class : textinputclass
            """
            'auther': forms.TextInput(attrs={'class': 'textinputclass'}),
            # class : refer again. text area is somewhat pre defined. its connected to css class.
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
