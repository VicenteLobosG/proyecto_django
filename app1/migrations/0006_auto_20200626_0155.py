# Generated by Django 3.0.7 on 2020-06-26 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_carrito_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto', models.IntegerField(default=1)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Producto')),
            ],
        ),
        migrations.RemoveField(
            model_name='carrito',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='producto',
        ),
        migrations.AddField(
            model_name='carrito',
            name='venta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.Venta'),
        ),
        migrations.AddField(
            model_name='venta',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='DetalleVenta',
        ),
        migrations.AddField(
            model_name='carrito',
            name='orden',
            field=models.ManyToManyField(to='app1.OrdenCompra'),
        ),
    ]
