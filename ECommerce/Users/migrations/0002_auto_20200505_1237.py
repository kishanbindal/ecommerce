# Generated by Django 3.0.2 on 2020-05-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone_number',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
