# Generated by Django 2.2 on 2019-10-26 10:57

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0004_auto_20191022_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminderdb',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='Asia/Kolkata'),
        ),
    ]
