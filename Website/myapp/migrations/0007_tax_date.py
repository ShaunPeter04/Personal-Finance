# Generated by Django 3.0 on 2025-02-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_income_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tax',
            name='Date',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
