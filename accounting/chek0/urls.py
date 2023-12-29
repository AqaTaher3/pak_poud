from django.urls import path
from . import views

app_name = 'chek'
urlpatterns = [
    # path('cheks/', views.cheks_page, name='cheks'),
    path('crete/', views.create_chek, name='create'),
    path('profile/<int:pk>', views.chek_profile, name='profile'),
    # path('update/<str:pk>/', views.update_sayad, name='update'),
    # path('delete/<str:pk>/', views.delete_chek, name='delete'),
]
