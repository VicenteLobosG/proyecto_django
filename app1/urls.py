from app1 import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

app_name='fiesta'

urlpatterns = [
    path('', views.home, name="home"),
    path('articulos', views.articulos, name="articulos"),
    path('carrito', views.carrito, name="carrito"),
    path('addproducto/<int:producto_id>', views.addproducto, name='addproducto'),
    path('quitarproducto/<int:producto_id>', views.quitarproducto, name='quitarproducto'),
    path('comprar/<int:pk>', views.comprar, name="comprar"),
    path('vaciar', views.vaciar, name="vaciar"),
    path('compras', views.compras, name="compras"),
    path('masproducto', views.masproducto, name="masproducto"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
]