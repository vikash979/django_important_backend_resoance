# Generated by Django 2.2.9 on 2020-02-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjecthasunit',
            name='label',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
