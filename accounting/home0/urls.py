from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    # path('create/', views.create_moshtari, name='create'),
    # path('delete/<str:pk>/', views.delete_moshtari, name='delete'),
    # path('profile/<int:pk>/', views.moshtari_profile, name='profile'),
    # path('update/<str:pk>/', views.update_moshtari, name='update'),
]
