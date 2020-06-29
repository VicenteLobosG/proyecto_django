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
    path('comprar', views.comprar, name="comprar"),
]