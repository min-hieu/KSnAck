# Generated by Django 3.0.5 on 2020-05-17 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='method',
            field=models.IntegerField(choices=[(0, 'Request'), (1, 'Offer')], default=0),
        ),
    ]
