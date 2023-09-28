# Generated by Django 3.1.6 on 2023-09-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='image1',
            field=models.ImageField(upload_to='actors_images'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='actors_images'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='actors_images'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='actors_images'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image1',
            field=models.ImageField(upload_to='movies_images'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='movies_images'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='movies_images'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='movies_images'),
        ),
    ]