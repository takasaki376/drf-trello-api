# Generated by Django 3.1 on 2020-11-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='text',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
