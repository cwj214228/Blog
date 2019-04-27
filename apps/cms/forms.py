from django import forms
from apps.article.models import Article
from apps.forms import FormMimin
from django.views.generic import View


class EditArticleCategoryForm(forms.Form):
    pk = forms.IntegerField()
    name = forms.CharField(max_length=50)


class EditArticleForm(forms.ModelForm, FormMimin):
    category = forms.IntegerField()
    pk = forms.IntegerField()

    class Meta:
        model = Article
        exclude = ['category', 'pub_time']


class WriteArticleForm(forms.ModelForm, FormMimin):
    category = forms.IntegerField()

    # pk = forms.IntegerField()

    class Meta:
        model = Article
        exclude = ['category', 'pub_time']