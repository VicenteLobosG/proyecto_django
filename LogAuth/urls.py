from django.urls import path
from LogAuth import views



app_name='auth'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('update_user/<int:pk>', views.update_user, name='update_user'),
]