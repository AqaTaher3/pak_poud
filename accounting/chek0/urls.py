from django.urls import path
from . import views

app_name = 'chek'
urlpatterns = [
    path('cheks/', views.kole_chek_ha, name='home'),
    path('profile/<int:pk>', views.chek_profile, name='profile'),
    path('create/', views.create_chek, name='create'),
    path('update/<str:pk>/', views.update_chek, name='update'),
    path('delete/<str:pk>/', views.delete_chek, name='delete'),
]
