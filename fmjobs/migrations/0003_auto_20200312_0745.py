# Generated by Django 3.0.3 on 2020-03-11 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmjobs', '0002_auto_20200311_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link1title',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='link2title',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='link3title',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='link4title',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='link5title',
            field=models.TextField(null=True),
        ),
    ]
