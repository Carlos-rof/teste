# Generated by Django 4.2 on 2023-04-05 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.TextField()),
                ('message', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]