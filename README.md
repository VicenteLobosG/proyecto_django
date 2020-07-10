# Proyecto de curso

Este proyecto está hecho a partir de la situación del bazar _"Mi Fiesta"_ ubicado en el centro de Rancagua al frente del instituto regional de educación. Para efectos del ramo las ventas fueron simuladas. El proyecto consiste en un sitio de ventas web, el cual cuenta con los siguientes módulos y funcionalidades:

* Sistema de Usuario
   * Login
   * Registro
   * Logout
   * Editar cuenta

* Venta
   * Agregar item al carrito
   * Eliminar item del carrito
   * Ver carrito
   * Realizar compra
   * Ver compras realizadas

* Admin
   * Agregar produto
   * Eliminar produto
   * Editar producto
   * Ver productos
   * Actualizar inventario
   * Ver compras de los usuarios

## Dependencias de la aplicación

La aplicación tiene las siguientes dependencias

* Python = 3.8.3

 Para instalar python dirigirse al siguiente sitio:

 [Python](https://www.python.org/downloads/)

* Django = 3.0.7

 Para instalar django introducir la siguiente linea en la terminal

 ```bash
 pip install django=3.0.7
 ```

* Djago-Bootstrap4 = 2.0.1

 Para instalar django-bootstrap4 introducir la siguiente linea en la terminal

 ```bash
 pip install django-bootstrap4=2.0.1
 ```

##Uso de la aplicación

Para levantar el aplicativo web, abrir terminal en la carpeta raíz y escribir la siguiente linea:

```bash
python manage.py runserver
```

Punto de entrada de la aplicación:

[Bazar Mi Fiesta](http://localhost:8000/login/)

## Lista de usuarios

| Usuario        | Contraseña    |
| -------------- |:-------------:|
| root           | toor          |
| Usuario_Prueba | abcd1234      |