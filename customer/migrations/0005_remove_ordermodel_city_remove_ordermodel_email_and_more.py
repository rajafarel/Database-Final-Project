# Generated by Django 4.2.7 on 2023-12-02 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='state',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='street',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='zip_code',
        ),
    ]
