# Generated by Django 3.2.5 on 2021-07-14 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_post_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reply',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
