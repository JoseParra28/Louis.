# Generated by Django 3.2 on 2023-05-08 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='status',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, max_length=150),
        ),
    ]
