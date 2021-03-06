# Generated by Django 3.2.8 on 2021-11-03 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mon', models.CharField(default=None, max_length=500)),
                ('tue', models.CharField(default=None, max_length=500)),
                ('wed', models.CharField(default=None, max_length=500)),
                ('thu', models.CharField(default=None, max_length=500)),
                ('fri', models.CharField(default=None, max_length=500)),
                ('sat', models.CharField(default=None, max_length=500)),
                ('sun', models.CharField(default=None, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('manager', 'MANAGER'), ('guard', 'GUARD')], default='guard', max_length=50)),
                ('user', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Guard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AllowedHolidays', models.IntegerField(default=4)),
                ('requestst', models.IntegerField(default=0)),
                ('requestdone', models.IntegerField(default=0)),
                ('requestmsg', models.CharField(default=None, max_length=500, null=True)),
                ('date', models.CharField(default=None, max_length=15, null=True)),
                ('manno', models.CharField(max_length=500, null=True)),
                ('user', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
