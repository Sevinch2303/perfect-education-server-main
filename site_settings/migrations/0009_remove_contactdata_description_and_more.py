# Generated by Django 4.1.1 on 2022-09-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0008_contactdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactdata',
            name='description',
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='address',
            field=models.TextField(max_length=600),
        ),
    ]
