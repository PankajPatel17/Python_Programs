# Generated by Django 5.1.1 on 2024-09-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='Buyer', max_length=100),
        ),
    ]
