from django import forms
#from tinymce import TinyMCE
from .models import Post, Comment



class PostModelForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'overview', 'thumbnail', 'categories', 'featured', 'previous_post', 'next_post']

class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control',
		'placeholder': 'Tapez votre commentaire',
		'id': ' usercomment',
		'rows': '4'
		}))
	class Meta:
		model = Comment
		fields = ('content', )