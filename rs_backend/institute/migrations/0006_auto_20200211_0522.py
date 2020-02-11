# Generated by Django 2.2.9 on 2020-02-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0005_remove_sessions_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programs',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='programs',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, 'online'), (2, 'dist_program'), (3, 'offline')], default=1),
        ),
    ]