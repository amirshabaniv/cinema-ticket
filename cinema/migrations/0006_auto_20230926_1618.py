# Generated by Django 3.1.6 on 2023-09-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_auto_20230925_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='elevator',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='cinema',
            name='parking',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
