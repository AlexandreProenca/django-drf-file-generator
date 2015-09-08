django-drf-file-generator
=======

.. image:: https://pypip.in/v/drf-gem/badge.png
    :target: https://pypi.python.org/pypi/drf-gem
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/AlexandreProenca/drf-gem.png
   :target: https://travis-ci.org/AlexandreProenca/drf-gem
   :alt: Latest Travis CI build status


           ╔╦╗ ┬┌─┐┌┐┌┌─┐┌─┐  ╔╦╗╦═╗╔═╗  ┌─┐┬  ┌─┐  ┌─┐┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
            ║║ │├─┤││││ ┬│ │   ║║╠╦╝╠╣   ├┤ │  ├┤   │ ┬├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
           ═╩╝└┘┴ ┴┘└┘└─┘└─┘  ═╩╝╩╚═╚    └  ┴─┘└─┘  └─┘└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─


Django DRF File Generation provides a safe way to generate automatically django basic files like url.py, serializers.py, admin.py, views.py, to use with djangorestframework, based on your models.py


Free software: MIT license

GitHub: https://github.com/AlexandreProenca/drf-gem

Documentation: http://drf-gem.readthedocs.org/



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
  
  $ python drf-gem -a -s -m path/my/models.py
  
  $ python drf-gem -m path/my/models.py --views --serializers
  
  $ python drf-gem -m path/my/models.py --clean
  
  $ python drf-gem -m path/my/models.py --All
  



Installation
------------
Easiest way to install this library is by using pip:
    $ pip install drf-file-gem

Requirements
^^^^^^^^^^^^
    * Python 2.7, 3.x, pypy or pypy3
    * Django 1.8+ (there are plans to support older Django versions)
    * Django REST Framework 2 or 3


Authors
-------

`django-drf-file-generator` was written by `Alexandre Proença <alexandre.proenca@hotmail.com.br>`_.
