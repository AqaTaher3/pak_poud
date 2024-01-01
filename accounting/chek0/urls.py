from django.urls import path
from . import views

app_name = 'chek'
urlpatterns = [
    path('home/', views.kole_chek_ha, name='home'),
    path('profile/<int:id>', views.chek_profile, name='profile'),
    path('create/', views.create_chek, name='create'),
    path('update/<str:id>/', views.update_chek, name='update'),
    path('delete/<str:id>/', views.delete_chek, name='delete'),
]
