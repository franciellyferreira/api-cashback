from django.urls import path
from django.conf.urls import url, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView,
)

from . import views


urlpatterns = [
    # gera token para autenticacao jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # verifica se o token é válido
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # endpoints do Revendedor
    url(r'^revendedores/$', views.RevendedorCreate.as_view(), name='revendedor-create'),
    url(r'^revendedores/login/$', views.revendedor_login, name='revendedor-login'),
    # endpoints da Compra
    url(r'^compras/$', views.CompraListCreate.as_view(), name='compra-list-create'),
    url(r'^compras/(?P<pk>[0-9]+)/$', views.CompraUpdateDelete.as_view(), name='compra-update-delete'),
    url(r'^compras/cashback/$', views.cashback_list, name='list-cashback'),
]
