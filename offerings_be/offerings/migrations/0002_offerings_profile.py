# Generated by Django 2.1.5 on 2019-02-05 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
        ('offerings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerings',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profile.Profile'),
        ),
    ]