# Generated by Django 5.0.3 on 2024-04-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
