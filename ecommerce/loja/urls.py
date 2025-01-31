from django.urls import path
from .views import (
    FornecedorCreateView, CategoriaCreateView, ProdutoCreateView,
    FornecedorListView, CategoriaListView, ProdutoListView
)

urlpatterns = [
    path('cadastrar-fornecedor/', FornecedorCreateView.as_view(), name='cadastrar_fornecedor'),
    path('cadastrar-categoria/', CategoriaCreateView.as_view(), name='cadastrar_categoria'),
    path('cadastrar-produto/', ProdutoCreateView.as_view(), name='cadastrar_produto'),
    path('listar-fornecedores/', FornecedorListView.as_view(), name='listar_fornecedores'),
    path('listar-categorias/', CategoriaListView.as_view(), name='listar_categorias'),
    path('listar-produtos/', ProdutoListView.as_view(), name='listar_produtos'),
]   