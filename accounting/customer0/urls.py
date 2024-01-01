from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('home/', views.kole_customer_ha, name='home'),
    path('profile/<int:pk>', views.customer_profile, name='profile'),
    path('delete/<int:pk>/', views.delete_customer, name='delete'),
    path('update/<int:pk>/', views.update_customer, name='update'),
    path('create/', views.create_customer, name='create'),
]
