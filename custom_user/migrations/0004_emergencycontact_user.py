# Generated by Django 5.0.3 on 2024-03-28 16:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_emergencycontact_remove_user_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencycontact',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact', to=settings.AUTH_USER_MODEL),
        ),
    ]
