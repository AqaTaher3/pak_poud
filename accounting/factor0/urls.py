from django.urls import path
from . import views

app_name = 'factor'
urlpatterns = [
    path('home/', views.kole_factor_ha, name='home'),
    path('profile/<int:id>', views.factor_profile, name='profile'),
    path('delete/<int:id>/', views.delete_factor, name='delete'),
    path('update/<int:pk>/', views.InvoiceUpdateView.as_view(), name='update'),
    path('create/', views.create_factor, name='create'),
    path('rools-of-factor/<int:factor_id>', views.tage_haye_factor, name='tage_factor'),
    path('anbar/', views.mojoodi_anbar, name='anbar'),
    path('tage-create/', views.RollCreateView.as_view(), name='create_tage'),


]
