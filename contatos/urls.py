from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contato_id>', views.ver_contato, name='contato'),
    path('busca/', views.busca, name='busca'),
    path('accounts/', include('accounts.urls')),
]