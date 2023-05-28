import factory
from factory.fuzzy import FuzzyDecimal, FuzzyInteger

from core.models import Categoria, Cidade, Cliente, Compras, Endereco, Fornecedor, Funcionario, Pais, Pedido, Produto

class PaisFactory(factory.django.DjangoModelFactory):
    nome = factory.Faker('country')

    class Meta:
        model = Pais
        django_get_or_create = ('nome',)

class CidadeFactory(factory.django.DjangoModelFactory):
    nome = factory.Faker('city', locale="pt_BR")
    pais = factory.SubFactory(PaisFactory)

    class Meta:
        model = Cidade
        django_get_or_create = ('nome', )

class EnderecoFactory(factory.django.DjangoModelFactory):
    rua = factory.Faker('street_address', locale="pt_BR")
    cidade = factory.SubFactory(CidadeFactory)
    cep = factory.Faker('postcode', locale="pt_BR")

    class Meta:
        model = Endereco
        django_get_or_create = ('cep', )


class CategoriaFactory(factory.django.DjangoModelFactory):
    nome = factory.Faker('word', locale="pt_BR")

    class Meta:
        model = Categoria
        django_get_or_create = ('nome', )

class ClienteFactory(factory.django.DjangoModelFactory):
    nome = factory.Faker('name', locale="pt_BR")
    telefone = factory.Faker('phone_number', locale="pt_BR")
    email = factory.Faker('email', locale="pt_BR")

    @factory.post_generation
    def enderecos(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for endereco in extracted:
                self.enderecos.add(endereco)

    class Meta:
        model = Cliente
        django_get_or_create = ('nome', 'email')

class FuncionarioFactory(factory.django.DjangoModelFactory):
    nome = factory.Faker('name', locale="pt_BR")
    telefone = factory.Faker('phone_number', locale="pt_BR")
    email = factory.Faker('email', locale="pt_BR")
    cargo = factory.Faker('job', locale="pt_BR")

    @factory.post_generation
    def enderecos(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for endereco in extracted:
                self.enderecos.add(endereco)

    class Meta:
        model = Funcionario
        django_get_or_create = ('nome', )


class ProdutoFactory(factory.django.DjangoModelFactory):
    nome = factory.Faker('word', locale="pt_BR")
    descricao = factory.Faker('sentence', nb_words=6, locale="pt_BR")
    preco_venda = FuzzyDecimal(1, 100)
    preco_custo = FuzzyDecimal(1, 100)
    quantidade = FuzzyInteger(0, 1000)
    categoria = factory.SubFactory(CategoriaFactory)

    class Meta:
        model = Produto
        django_get_or_create = ('nome', )

class FornecedorFactory(factory.django.DjangoModelFactory):
    nome = factory.Faker('company', locale="pt_BR")
    telefone = factory.Faker('phone_number', locale="pt_BR")
    email = factory.Faker('email', locale="pt_BR")
    cnpj = factory.Faker('numerify', text='##############', locale="pt_BR")

    @factory.post_generation
    def enderecos(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for endereco in extracted:
                self.enderecos.add(endereco)

    @factory.post_generation
    def produtos(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for produto in extracted:
                self.produtos.add(produto)

    class Meta:
        model = Fornecedor
        django_get_or_create = ('nome', )

class PedidoFactory(factory.django.DjangoModelFactory):
    data_pedido = factory.Faker('date_between', start_date='-1y', end_date='today')
    quantidade = FuzzyInteger(1, 100)
    preco_total = FuzzyDecimal(1, 10000)
    cliente = factory.SubFactory(ClienteFactory)
    funcionario = factory.SubFactory(FuncionarioFactory)

    class Meta:
        model = Pedido
        django_get_or_create = ('data_pedido', 'cliente',)

class ComprasFactoryy(factory.django.DjangoModelFactory):
    data_compra = factory.Faker('date_between', start_date='-1y', end_date='today')
    quantidade = FuzzyInteger(1, 10)
    fornecedor = factory.SubFactory(FornecedorFactory)

    @factory.post_generation
    def produtos(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for produto in extracted:
                self.produtos.add(produto)
    class Meta:
        model = Compras
        django_get_or_create = ('data_compra', 'fornecedor',)
