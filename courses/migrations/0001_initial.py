# Generated by Django 5.0.3 on 2024-04-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50)),
                ('class_date', models.DateTimeField()),
                ('class_length', models.DurationField(null=True)),
                ('class_location', models.CharField(max_length=50)),
                ('class_code', models.CharField(max_length=10)),
            ],
        ),
    ]
