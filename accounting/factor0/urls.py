from django.urls import path
from . import views

app_name = 'factor'
urlpatterns = [
    path('home/', views.kole_factor_ha, name='home'),
    path('create/', views.create_factor, name='create'),
    path('profile/<int:pk>', views.factor_profile, name='profile'),
    path('update/<str:pk>/', views.update_factor, name='update'),
    path('delete/<str:pk>/', views.delete_factor, name='delete'),
]
