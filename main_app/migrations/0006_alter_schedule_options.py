# Generated by Django 4.0.5 on 2022-06-08 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_schedule_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['-day', 'time']},
        ),
    ]