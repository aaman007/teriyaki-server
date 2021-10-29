# Generated by Django 3.2.8 on 2021-10-29 13:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='managers',
            field=models.ManyToManyField(related_name='vendors', to=settings.AUTH_USER_MODEL, verbose_name='Managers'),
        ),
    ]
