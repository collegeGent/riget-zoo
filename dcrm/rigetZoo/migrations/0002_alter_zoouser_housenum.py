# Generated by Django 4.2.16 on 2024-11-13 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rigetZoo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zoouser',
            name='houseNum',
            field=models.IntegerField(null=True),
        ),
    ]