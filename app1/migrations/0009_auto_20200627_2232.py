# Generated by Django 3.0.7 on 2020-06-28 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20200627_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordencompra',
            name='cantidad_producto',
            field=models.IntegerField(default=1),
        ),
    ]
