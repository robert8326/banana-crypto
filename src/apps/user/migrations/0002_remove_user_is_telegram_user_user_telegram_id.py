# Generated by Django 4.2.2 on 2023-06-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_telegram_user',
        ),
        migrations.AddField(
            model_name='user',
            name='telegram_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Telegram id'),
        ),
    ]
