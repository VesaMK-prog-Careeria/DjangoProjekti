from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', views.etusivu, name='etusivu'),  # Aloitussivu
    path('tyontekija/lisaa/', views.tyontekija_lisays, name='tyontekija_lisays'),
    path('kalusto/', views.kalusto_lista, name='kalusto_lista'),
    path('tyomaat/', views.tyomaa_lista, name='tyomaa_lista'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('kalusto/lisaa/', views.kalusto_lisays, name='kalusto_lisays'),
    path('kalusto/muokkaa/<int:pk>/', views.kalusto_muokkaus, name='kalusto_muokkaus'),
    path('kalusto/poista/<int:pk>/', views.kalusto_poisto, name='kalusto_poisto'),
    path('tyomaat/lisaa/', views.tyomaa_lisays, name='tyomaa_lisays'),
    path('tyomaat/muokkaa/<int:pk>/', views.tyomaa_muokkaus, name='tyomaa_muokkaus'),
    path('tyomaat/poista/<int:pk>/', views.tyomaa_poisto, name='tyomaa_poisto'),
]