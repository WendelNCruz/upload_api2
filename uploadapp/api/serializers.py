from rest_framework.serializers import ModelSerializer
from uploadapp.models import Pessoa


class PessoaSerializer(ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'sobrenome',
                  'sexo', 'altura', 'peso',
                  'nascimento', 'bairro', 'cidade',
                  'estado', 'numero')


class PSexoSerializer(ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'sobrenome',
                  'sexo', 'altura', 'peso',
                  'nascimento', 'bairro', 'cidade',
                  'estado', 'numero')
