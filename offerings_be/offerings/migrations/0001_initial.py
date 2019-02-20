# Generated by Django 2.1.5 on 2019-02-20 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offerings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('description', models.TextField()),
                ('phone', models.IntegerField()),
                ('distance', models.IntegerField(default=None)),
                ('notify', models.BooleanField(default=False)),
                ('image', models.URLField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profile.Profile')),
            ],
        ),
    ]
