from django.db import models

class Pais(models.Model):
    nome = models.TextField(verbose_name="Nome", max_length=255)

class Cidade(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=255)
    pais = models.ForeignKey("core.Pais", verbose_name="Pais", on_delete=models.CASCADE, related_name='cidades')

class Endereco(models.Model):
    rua = models.CharField(verbose_name="Rua", max_length=255)
    cidade = models.ForeignKey("core.Cidade", verbose_name="Cidade", on_delete=models.CASCADE, related_name='enderecos')
    cep = models.CharField(verbose_name="CEP", max_length=9)

class Categoria(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=255)

class Cliente(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=255)
    telefone = models.CharField(verbose_name="Telefone", max_length=20)
    email = models.EmailField(verbose_name="Email", max_length=254)
    enderecos = models.ManyToManyField("core.Endereco", verbose_name="Enderecos", related_name="clientes")

class Funcionario(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=255)
    telefone = models.CharField(verbose_name="Telefone", max_length=20)
    email = models.EmailField(verbose_name="Email", max_length=254)
    enderecos = models.ManyToManyField("core.Endereco", verbose_name="Enderecos", related_name="funcionarios")
    cargo = models.CharField(verbose_name="Cargo", max_length=255)

class Produto(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100)
    descricao = models.CharField(verbose_name="Nome", max_length=200)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveSmallIntegerField(verbose_name="Quantidade")
    categoria = models.ForeignKey("core.Categoria",  on_delete=models.CASCADE, related_name="produtos")

class Fornecedor(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=255)
    telefone = models.CharField(verbose_name="Telefone", max_length=20)
    email = models.EmailField(verbose_name="Email", max_length=254)
    enderecos = models.ManyToManyField("core.Endereco", verbose_name="Enderecos", related_name="fornecedores")
    cnpj = models.CharField(verbose_name="Nome", max_length=20)
    produtos = models.ManyToManyField("core.Produto", related_name="fornecedor")

class Pedido(models.Model):
    data_pedido = models.DateField(verbose_name="Data Pedido", auto_now=False, auto_now_add=False)
    quantidade = models.PositiveSmallIntegerField(verbose_name="Quantidade")
    preco_total = models.DecimalField(verbose_name="Preco Total", max_digits=10, decimal_places=2)
    cliente = models.ForeignKey("core.Cliente", verbose_name="Cliente", on_delete=models.CASCADE, related_name="pedidos")
    funcionario = models.ForeignKey("core.Funcionario", on_delete=models.CASCADE, related_name='pedidos')

class Compras(models.Model):
    data_compra = models.DateField(verbose_name="Data Pedido", auto_now=False, auto_now_add=False)
    quantidade = models.PositiveSmallIntegerField(verbose_name="Quantidade")
    fornecedor = models.ForeignKey("core.Fornecedor", on_delete=models.CASCADE, related_name="compras")
    produtos = models.ManyToManyField("core.Produto", related_name="compras")
