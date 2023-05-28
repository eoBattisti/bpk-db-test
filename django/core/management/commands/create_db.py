import logging
from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from core.management.commands.builders import builder


LOGGER = logging.getLogger(__name__)

class Command(BaseCommand):
    cache = {}
    size = 1000

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--size',
                            action='store',
                            dest='size',
                            default=1000,
                            type=int)

    def handle(self, *args, **options):
        self.size = options['size']

        print("Creating paises")
        builder.create_paises(self)

        print("Creating cidades")
        builder.create_cidades(self)

        print("Creating enderecos")
        builder.create_endereco(self)

        print("Creating clientes")
        builder.create_cliente(self)

        print("Creating funcionairos")
        builder.create_funcionarios(self)

        print("Creating categorias")
        builder.create_categoria(self)

        print("Creating produtos")
        builder.create_produto(self)

        print("Creating fornecedores")
        builder.create_fornecedores(self)

        print("Creating compras")
        builder.create_compras(self)

        print("Creating pedidos")
        builder.create_pedidos(self)
