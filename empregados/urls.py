from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:empregado_id>', views.empregado, name='empregado'),
    path('busca/', views.busca, name='busca'),
    path('accounts/', include('accounts.urls')),
]