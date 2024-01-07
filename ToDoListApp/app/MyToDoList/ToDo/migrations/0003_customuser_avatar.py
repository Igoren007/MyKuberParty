# Generated by Django 4.0.3 on 2022-03-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0002_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='../static/ToDo/images/default.png', upload_to='media/', verbose_name='Avatar'),
        ),
    ]
