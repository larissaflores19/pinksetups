# Generated by Django 3.1.7 on 2021-03-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinksetup', '0007_remove_favorites_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='vote',
            field=models.IntegerField(default=0, verbose_name=(1, 2)),
        ),
    ]
