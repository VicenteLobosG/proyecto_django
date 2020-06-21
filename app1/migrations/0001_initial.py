# Generated by Django 3.0.7 on 2020-06-21 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LogAuth', '0002_auto_20200620_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('hora_act', models.DateTimeField(verbose_name='fecha de actualizacion')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_p', models.CharField(max_length=200)),
                ('fecha_exp', models.DateTimeField(verbose_name='fecha de expiracion')),
                ('precio', models.IntegerField(default=1)),
                ('inventario', models.ManyToManyField(to='app1.Inventario')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_t', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_venta', models.DateTimeField(verbose_name='hora venta')),
                ('producto', models.ManyToManyField(to='app1.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Tipo'),
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto', models.IntegerField(default=1)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ManyToManyField(to='app1.Producto')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LogAuth.Profile')),
            ],
        ),
    ]