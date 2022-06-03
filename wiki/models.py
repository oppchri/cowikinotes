from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=3, primary_key=True)
    label = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self) -> str:
        return self.label


class Page(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    category = models.ForeignKey(
        Category, default="NON", on_delete=models.SET_DEFAULT)
    description = RichTextUploadingField(blank=True, null=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SubPage(models.Model):
    name = models.CharField(max_length=100)
    page = models.ForeignKey(to=Page, on_delete=models.SET_NULL, null=True, )
    page_index = models.IntegerField(default=1)
    content = RichTextUploadingField(blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        to=User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.name
