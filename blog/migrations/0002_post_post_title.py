# Generated by Django 5.2.4 on 2025-07-13 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(default='bruh', max_length=100),
            preserve_default=False,
        ),
    ]
