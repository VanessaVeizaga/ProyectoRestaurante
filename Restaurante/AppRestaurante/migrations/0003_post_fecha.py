# Generated by Django 4.0.4 on 2022-05-02 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRestaurante', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(default='2022-05-02 19:22:11.517108'),
        ),
    ]