from rest_framework.viewsets import ModelViewSet
from .serializers import PessoaSerializer, PSexoSerializer
from uploadapp.models import Pessoa


class PessoaViewSet(ModelViewSet):
    serializer_class = PessoaSerializer

    def get_queryset(self):
        return Pessoa.objects.all().filter(cidade='Meeren', sexo='F')


class PSexoViewSet(ModelViewSet):
    serializer_class = PSexoSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        sexo = query_params.get('sexo', None)
        if sexo is not None:
            return Pessoa.objects.all().order_by('-nascimento').filter(sexo=sexo.upper())
        return Pessoa.objects.all().order_by('-nascimento')
