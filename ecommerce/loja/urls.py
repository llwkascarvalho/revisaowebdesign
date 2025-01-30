from django.urls import path
from .views import cadastrar_fornecedor, cadastrar_categoria, cadastrar_produto

urlpatterns = [
    path('cadastrar-fornecedor/', cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('cadastrar-categoria/', cadastrar_categoria, name='cadastrar_categoria'),
    path('cadastrar-produto/', cadastrar_produto, name='cadastrar_produto'),
]
