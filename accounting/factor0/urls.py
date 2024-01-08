from django.urls import path
from . import views

app_name = 'factor'
urlpatterns = [
    path('home/', views.kole_factor_ha, name='home'),
    path('profile/<int:id>', views.factor_profile, name='profile'),
    path('delete/<int:id>/', views.delete_factor, name='delete'),
    path('update/<int:id>/', views.update_factor, name='update'),
    path('create/', views.create_factor, name='create'),
    path('create/<int:factor_id>', views.tage_haye_factor, name='tage_factor'),
]
