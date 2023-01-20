from import_export import resources
from .models import Pessoa


class PessoaResource(resources.ModelResource):
    class Meta:
        model = Pessoa
