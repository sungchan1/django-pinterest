from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreateForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'editable text-start', 'style': 'height: auto;'}))

    project = forms.ModelChoiceField(Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
