from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from uploadapp.models import Pessoa


@admin.register(Pessoa)

class PessoaAdmin(ImportExportModelAdmin):
    list_display = ('nome', 'sobrenome', 'sexo',
                    'altura', 'peso', 'nascimento',
                    'bairro', 'cidade', 'estado', 'numero')