# Generated by Django 3.0 on 2025-03-06 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_delete_expenses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Expenses', models.CharField(max_length=100)),
                ('Month', models.CharField(max_length=100)),
                ('Year', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Discription', models.CharField(max_length=100)),
                ('Type', models.CharField(default='', max_length=100)),
                ('BUDGET', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Budget')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User')),
            ],
        ),
    ]
