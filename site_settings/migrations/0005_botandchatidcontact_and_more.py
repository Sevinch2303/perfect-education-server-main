# Generated by Django 4.1.1 on 2022-09-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0004_botandchatid'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotAndChatIdContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Bot Token And Chat ID', max_length=600)),
                ('bot_token', models.CharField(max_length=1000)),
                ('chat_id', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Telegram Bot Data Contact',
                'verbose_name_plural': 'Telegram Bot Data Contact',
            },
        ),
        migrations.RenameModel(
            old_name='BotAndChatId',
            new_name='BotAndChatId2Course',
        ),
        migrations.AlterModelOptions(
            name='botandchatid2course',
            options={'verbose_name': 'Telegram Bot Data Course', 'verbose_name_plural': 'Telegram Bot Data Course'},
        ),
    ]
