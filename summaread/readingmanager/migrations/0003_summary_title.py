# Generated by Django 3.0.4 on 2020-03-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readingmanager', '0002_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='title',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
