# Generated by Django 3.2.8 on 2021-11-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secure_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guard',
            name='requestdone',
            field=models.CharField(default=0, max_length=10, null=True),
        ),
    ]
