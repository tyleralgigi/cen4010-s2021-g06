from django import forms
from users.models import User


class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=256, required=False)


class ReportForm(forms.Form):
    report_description = forms.CharField(max_length=512, required=False)


class RemovePostForm(forms.Form):
    post_id = forms.IntegerField()
