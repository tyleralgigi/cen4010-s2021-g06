from django import forms


class PostForm(forms.Form):
    description = forms.CharField(max_length=256, required=False)
    image = forms.ImageField()


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=256)
