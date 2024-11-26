# Generated by Django 5.1.3 on 2024-11-26 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rigetZoo', '0003_hotelbooking_zoobooking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelbooking',
            name='adult',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='child',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='zoobooking',
            name='adult',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='zoobooking',
            name='child',
            field=models.IntegerField(default=0),
        ),
    ]