# Generated by Django 2.0.5 on 2018-05-14 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workarea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.CharField(default='enoch_1', max_length=30, unique=True),
            preserve_default=False,
        ),
    ]