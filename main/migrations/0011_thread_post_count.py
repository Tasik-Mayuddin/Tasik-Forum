# Generated by Django 3.2.5 on 2021-07-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210716_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='post_count',
            field=models.IntegerField(null=True),
        ),
    ]
