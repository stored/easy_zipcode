.. easyzipcode documentation master file, created by
   sphinx-quickstart on Fri Dec  5 16:39:23 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CEP
=======================================

Consulta de CEP
---------------------------------------
| A consulta a ser feita mostrará as informações do CEP correspondente. As informações são:
* Cidade;
* Código IBGE da Cidade;
* Bairro;
* Complemento;
* Endereço;
* CEP;
|
URL:
::
    http://localhost:8000/api/69908740/?token=2391f5a5-1962-4286-84bf-5189e83a59be
::

Variáveis:
::
    - 69908740: CEP a ser consultado
    - 2391f5a5-1962-4286-84bf-5189e83a59be: token
::

Retorno:
::
    {
        objects: [
            {
                city: "Rio Branco",
                ibge: "1200401",
                area: "Loteamento Santa Helena",
                complement: "",
                address: "Rua A",
                zip_code: "69908740"
            }
        ]
    }
::
