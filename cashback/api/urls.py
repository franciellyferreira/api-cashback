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
    # atualiza o tempo de vida do token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # endpoints do Revendedor
    url(r'^revendedores/$', views.RevendedorCreate.as_view(), name='revendedor-create'),
    url(r'^revendedores/login/$', views.revendedor_login, name='revendedor-login'),
]
