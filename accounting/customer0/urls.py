from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('profile/<int:pk>/', views.moshtari_profile, name='profile'),

    path('create/', views.create_moshtari, name='create'),
    # path('delete/<str:pk>/', views.delete_moshtari, name='delete'),
    # path('update/<str:pk>/', views.update_moshtari, name='update'),
]
