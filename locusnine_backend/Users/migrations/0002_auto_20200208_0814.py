# Generated by Django 3.0.3 on 2020-02-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='mobile_no',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
