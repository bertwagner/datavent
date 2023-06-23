# Generated by Django 4.2.1 on 2023-05-29 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=400)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('is_agreed_coc', models.BooleanField()),
                ('registration_date', models.DateTimeField(verbose_name='date registered')),
            ],
        ),
    ]
