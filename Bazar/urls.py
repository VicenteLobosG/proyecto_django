from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('LogAuth.urls'))
=======
    path('', include('LogAuth.urls')),
    path('app1/', include('app1.urls')),

>>>>>>> acb27ce7fa1f8b24c3ec6d86fdd2cab1240352f8
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
