# Generated by Django 3.2.16 on 2022-10-29 09:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0004_auto_20221029_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='replier',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
