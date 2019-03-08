# Generated by Django 2.1.5 on 2019-03-08 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offerings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profile.Profile')),
            ],
        ),
    ]
