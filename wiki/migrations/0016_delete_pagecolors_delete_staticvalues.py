# Generated by Django 4.0.4 on 2022-05-15 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0015_page_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PageColors',
        ),
        migrations.DeleteModel(
            name='StaticValues',
        ),
    ]
