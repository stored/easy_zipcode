.. easyzipcode documentation master file, created by
   sphinx-quickstart on Fri Dec  5 16:39:23 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Instalação
=======================================

Para instalar o easyzipcode, faça o download zip através do github:
::
    https://github.com/stored/easy_zipcode
::

Feito o download, descompacte-o no diretório de seu projeto e digite o seguinte comando:
::
    python setup.py install
::

Você também pode instalar através do pacote pip:
::
   pip install easy_zipcode
::

No arquivo settings.py de seu projeto, adicione a app easyzipcode:
::
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
::

Adicione a seguinte linha no arquivo urls.py do seu projeto:
::
    urlpatterns = patterns('',
        ...
        url(r'^easy_zipcode/', include(easyzipcode.urls())),
    )
::