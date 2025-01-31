from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Fornecedor, Categoria, Produto
from .forms import FornecedorForm, CategoriaForm, ProdutoForm

class HomeView(ListView):
    model = Produto
    template_name = 'home.html'
    context_object_name = 'produtos'

class FornecedorCreateView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'loja/cadastrar_fornecedor.html'
    success_url = reverse_lazy('cadastrar_fornecedor')

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'loja/cadastrar_categoria.html'
    success_url = reverse_lazy('cadastrar_categoria')

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'loja/cadastrar_produto.html'
    success_url = reverse_lazy('cadastrar_produto')

class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'loja/listar_fornecedores.html'
    context_object_name = 'fornecedores'

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'loja/listar_categorias.html'
    context_object_name = 'categorias'

class ProdutoListView(ListView):
    model = Produto
    template_name = 'loja/listar_produtos.html'
    context_object_name = 'produtos'