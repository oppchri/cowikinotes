from django.db import models
from colorfield.fields import ColorField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class SiteString(models.Model):
    key = models.CharField(max_length=20, primary_key=True)
    value = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.key


class SiteColor(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name


class SiteRichText(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    value = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.name
