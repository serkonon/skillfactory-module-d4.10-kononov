# Generated by Django 2.2.6 on 2020-11-14 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20201114_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
    ]
