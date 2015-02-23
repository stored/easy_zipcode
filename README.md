easyzipcode
===========

``easyzipcode`` é uma lib Python usada para retornar informações
de um determinado endereço a partir do CEP, com dados provenientes do webservice
``easyzipcode.io``

Para instalar o easyzipcode, faça o download zip através do github: ::

    https://github.com/stored/easy_zipcode

Feito o download, descompacte-o no diretório de seu projeto e digite o seguinte comando: ::
    
    python setup.py install

Você também pode instalar através do pacote pip: ::
   
    pip install easy_zipcode

Usando no terminal: ::
    
    >>> from easy_zipcode import EasyZipCode
    >>> print EasyZipCode.get_zipcode('14415000', token='3850de3a-2422-482...')
    {"city": "Patroc\u00ednio Paulista", "ibge": "3536307", "area": "", "complement": "", "address": "", "zip_code": "14415000"}

No arquivo ``settings.py`` de seu projeto, adicione a app easyzipcode e o token gerado: ::
    
    EASY_ZIPCODE_TOKEN = '3850de3a-2422-482d-92fc-d1a48a71eba1'

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        ...
        'easy_zipcode',
        ...
    )

Adicione a seguinte linha no arquivo ``urls.py`` do seu projeto: ::
    
    urlpatterns = patterns('',
        ...
        url(r'^easyzipcode/', include(easy_zipcode.urls())),
    )
