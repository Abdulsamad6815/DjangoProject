# Generated by Django 4.1 on 2022-10-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='is_deleted',
            field=models.CharField(default='n', max_length=2),
        ),
    ]
