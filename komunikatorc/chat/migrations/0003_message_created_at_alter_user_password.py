# Generated by Django 5.1.1 on 2024-09-13 17:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "chat",
            "0001_initial_squashed_0002_alter_friend_friend_alter_friend_user_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128),
        ),
    ]