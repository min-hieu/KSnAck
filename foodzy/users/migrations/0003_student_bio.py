# Generated by Django 3.0.5 on 2020-05-30 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200521_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='bio',
            field=models.TextField(default=''),
        ),
    ]
