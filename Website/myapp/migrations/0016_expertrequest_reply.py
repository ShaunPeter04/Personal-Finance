# Generated by Django 3.0 on 2025-02-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_expertrequest_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertrequest',
            name='reply',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
