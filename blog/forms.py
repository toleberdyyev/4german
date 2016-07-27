from django import forms
from .models import Post, Comment
from nocaptcha_recaptcha.fields import NoReCaptchaField

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    captcha=NoReCaptchaField()
    class Meta:
        model = Comment
        fields = ('text','parent')
