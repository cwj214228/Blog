from django import forms
from apps.article.models import Article


class EditArticleCategoryForm(forms.Form):
    pk = forms.IntegerField()
    name = forms.CharField(max_length=50)