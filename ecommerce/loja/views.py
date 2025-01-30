from django.shortcuts import render, redirect
from .forms import FornecedorForm, CategoriaForm, ProdutoForm

def home(request):
    return render(request, 'home.html')
def cadastrar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_fornecedor')
    else:
        form = FornecedorForm()
    return render(request, 'loja/cadastrar_fornecedor.html', {'form': form})

def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'loja/cadastrar_categoria.html', {'form': form})

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_produto')
    else:
        form = ProdutoForm()
    return render(request, 'loja/cadastrar_produto.html', {'form': form})
