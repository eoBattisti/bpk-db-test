from core.factories import (CategoriaFactory, CidadeFactory, ClienteFactory, ComprasFactoryy, EnderecoFactory,
                           FornecedorFactory, FuncionarioFactory, PaisFactory, PedidoFactory, ProdutoFactory)
import random
from core.models import Produto

def create_paises(command):
    paises = []
    for _ in range(193):
        pais = PaisFactory()
        paises.append(pais)
    command.cache['paises'] = paises

def create_cidades(command):
    cidades = []
    for pais in command.cache['paises']:
        for _ in range(command.size):
            cidade = CidadeFactory(pais=pais)
            cidades.append(cidade)

    command.cache['cidades'] = cidades

def create_endereco(command):
    enderecos = []
    for c in command.cache['cidades']:
        for _ in range(command.size):
            endereco = EnderecoFactory(cidade=c)
            enderecos.append(endereco)
    command.cache['enderecos'] = enderecos

def create_cliente(command):
    clientes = []
    for e in command.cache['enderecos']:
        for _ in range(command.size):
            cliente = ClienteFactory(enderecos=[e])
            clientes.append(cliente)
    command.cache['clientes'] = clientes

def create_funcionarios(command):
    funcionarios = []
    for _ in range(int(command.size / 2)):
        funcionairo = FuncionarioFactory()
        funcionarios.append(funcionairo)
    command.cache['funcionarios'] = funcionarios

def create_fornecedores(command):
    fornecedores = []
    for _ in range(command.size):
        produtos = []
        for p in command.cache['produtos']:
            if len(produtos) > 200:
                break
            produtos.append(random.choice(command.cache['produtos']))
        fornecedor = FornecedorFactory(produtos=produtos)
        fornecedores.append(fornecedor)
    command.cache['fornecedores'] = fornecedores

def create_categoria(command):
    categorias = []
    for _ in range(command.size):
        categoria = CategoriaFactory()
        categorias.append(categoria)
    command.cache['categorias'] = categorias

def create_produto(command):
    produtos = []
    for c in command.cache['categorias']:
        for _ in range(command.size):
            produto = ProdutoFactory(categoria=c)
            produtos.append(produto)
    command.cache['produtos'] = produtos

def create_compras(command):
    for f in command.cache['fornecedores']:
        for _ in range(command.size):
            produtos = []
            for i in range(4):
                available = Produto.objects.filter(fornecedor=f)
                if not available:
                    break
                produtos.append(random.choice(available))
            ComprasFactoryy(fornecedor=f, produtos=produtos)


def create_pedidos(command):
    for  _ in range(command.size):
        PedidoFactory(cliente=random.choice(command.cache['clientes']),
                      funcionario=random.choice(command.cache['funcionarios']))
