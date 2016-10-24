Django DRF File Generator
=======

.. image:: https://travis-ci.org/AlexandreProenca/django-drf-file-generator.svg?branch=master
        :target: https://travis-ci.org/AlexandreProenca/django-drf-file-generator

.. image:: https://img.shields.io/pypi/v/django-drf-file-generator.svg
        :target: https://pypi.python.org/pypi/django-drf-file-generator

.. image:: https://img.shields.io/pypi/dd/django-drf-file-generator.svg
        :target: https://pypi.python.org/pypi/django-drf-file-generator

.. image:: https://img.shields.io/pypi/pyversions/django-drf-file-generator.svg
        :target: https://pypi.python.org/pypi/django-drf-file-generator

.. image:: https://img.shields.io/pypi/l/django-drf-file-generator.svg
        :target: https://pypi.python.org/pypi/django-drf-file-generator

.. image:: https://img.shields.io/pypi/wheel/django-drf-file-generator.svg
        :target: https://pypi.python.org/pypi/django-drf-file-generator

.. image:: https://img.shields.io/pypi/format/django-drf-file-generator.svg
        :target: https://pypi.python.org/pypi/django-drf-file-generator

.. image:: https://img.shields.io/pypi/implementation/django-drf-file-generator.svg
        :target: https://pypi.python.org/pypi/django-drf-file-generator

.. image:: https://img.shields.io/pypi/status/django-drf-file-generator.svg
        :target: https://pypi.python.org/pypi/django-drf-file-generator

.. image:: https://api.codacy.com/project/badge/50515222d332430aba11bcbe76706f14
        :target: https://www.codacy.com/app/linuxloco/django-drf-file-generator

.. image:: https://readthedocs.org/projects/django-drf-file-generator/badge/?version=latest
        :target: http://django-drf-file-generator.readthedocs.org/en/latest/
        :alt: Documentation Status

.. image:: http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat
        :target: http://stackshare.io/AlexandreProenca/django-drf-file-generator
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/GITTER-join%20chat-green.svg
        :target: https://gitter.im/AlexandreProenca/devfriends?utm_source=share-link&utm_medium=link&utm_campaign=share-link
        :alt: Chat room



-----------

.. image:: https://img.shields.io/badge/english-ok-green.svg
        :target: https://img.shields.io/badge/english-ok-green.svg
        :alt: Documentation Status
        
Django DRF File Generator provides a safe way to generate automatically **Django basic files** like url.py, serializers.py, admin.py, views.py, to use with **djangorestframework**, the generated files will be based on your models.py 


.. image:: https://img.shields.io/badge/portugues--brasil-ok-green.svg
        :target: https://img.shields.io/badge/portugues--brasil-ok-green.svg
        :alt: Documentation Status
        
Django DRF Gerador de Arquivos, fornece uma maneira segura para gerar automaticamente **arquivos básicos do Django** como url.py, serializers.py, admin.py, views.py, para usar com **djangorestframework**, os arquivos gerados serão baseados em seu arquivo models.py.

Documentation: http://django-drf-file-generator.readthedocs.org/

Installation
------------
    Easiest way to install this library is by using pip:
    
    $ **pip install django-drf-file-generator**
    

Usage 
-----
Options:
   
   **-m path/my/models.py**   required parameter, path to models.py file
   
   **-a or --admin**          to create admin.py
   
   **-v or --views**          to create views.py
   
   **-u or --urls**           to create urls.py
   
   **-s or --serializers**    to create serializers.py
   
   **-A or --All**            to create urls.py, admin.py, views.py, serializers.py
   
   **-D or --clean**          warning!!! this option will remove gem_build directory and all files inside
   
   **-h or --help**           to show all options
   
Exemples:
  
  $ python drf-gen -m path/my/models.py --views --serializers
  
  $ python drf-gen -m path/my/models.py --clean
  
  $ python drf-gen -m path/my/models.py --All
  

Requirements
^^^^^^^^^^^^
    * Python 2.7, 3.4, pypy or pypy3
    * Django 1.8+ (there are plans to support older Django versions)
    * Django REST Framework 3.x


Authors
-------

`django-drf-file-generator` was written by `Alexandre Proença <alexandre.proenca@hotmail.com.br>`_.
