# Generated by Django 2.2.4 on 2020-02-29 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together=set(),
        ),
    ]