# Generated by Django 4.2.5 on 2023-11-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySelf', '0002_myself_admno_myself_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='myself',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]