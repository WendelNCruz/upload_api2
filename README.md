
# Django Conversor (Importar XLS para Banco de Dados)

Sistema desenvolvido para construção de API. 

Tecnologias: Python, Django, Django REST framework, HTML, CSS e JavaScript.


# Dependências(Requirements)

-  asgiref==3.6.0
-  defusedxml==0.7.1
-  diff-match-patch==20200713
- Django==4.1.5 
- django-import-export==3.0.2
- djangorestframework==3.14.0
- et-xmlfile==1.1.0
- MarkupPy==1.14
- odfpy==1.4.1
- openpyxl==3.0.10
- pytz==2022.7
- PyYAML==6.0
- sqlparse==0.4.3
- tablib==3.3.0
- xlrd==2.0.1
- xlwt==1.3.0







## Instalação

Instalar as bibliotecas/pacotes (no Linux):

```bash
sudo apt install -y libxml2 gcc python3-dev libxml2-dev libxslt1-dev zlib1g-dev python3-pip
sudo apt update
```

1 Gere um .env local


2 Instalar dependências:

```bash
pip install -r requirements.txt
```
3 Sincronize a base de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

4 Crie um usuário (Administrador do sistema):
```bash
python manage.py createsuperuser
```

5 Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):
```bash
python manage.py runserver
```

## Funcionalidades

- Upload de Arquios .XLS e .XLSX
- API com dois Endpoints:
    - GET: retornando mulheres de mereen.
    - GET: receber o sexo (m ou f) como parâmetro, filtrar e retornar a lista de pessoas, ordenada por idade.
- Exporta arquivos salvos

