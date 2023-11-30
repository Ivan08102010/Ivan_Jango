# Generated by Django 4.2.5 on 2023-11-29 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_pupil_gender_alter_pupil_class_p'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like_Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_Book', models.CharField(default='Book', max_length=30)),
                ('summary', models.CharField(default='Жили были и стали жить поживать да добра наживать', max_length=200)),
                ('Author', models.CharField(max_length=20)),
                ('date_born_author', models.DateTimeField(max_length=1)),
                ('date_create', models.DateTimeField(max_length=1)),
                ('interesting', models.BooleanField(default=True)),
                ('Genre', models.CharField(max_length=12)),
                ('size', models.FloatField(max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='pupil',
            name='bithday',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 29, 16, 44, 20, 756997, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='pupil',
            name='coming_of_age',
            field=models.BooleanField(default=True),
        ),
    ]