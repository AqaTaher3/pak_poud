from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('home/', views.kole_moshtari_ha, name='home'),
    path('profile/<int:id>/', views.moshtari_profile, name='profile'),
    path('delete/<str:pk>/', views.delete_moshtari, name='delete'),
    path('update/<str:pk>/', views.update_moshtari, name='update'),

    path('create/', views.create_moshtari, name='create'),
]
