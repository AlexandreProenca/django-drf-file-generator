drf-gem
=======

.. image:: https://pypip.in/v/drf-gem/badge.png
    :target: https://pypi.python.org/pypi/drf-gem
    :alt: Latest PyPI version

.. image:: ttps://travis-ci.org/AlexandreProenca/drf-gem.png
   :target: ttps://travis-ci.org/AlexandreProenca/drf-gem
   :alt: Latest Travis CI build status


  _____  _                           _____  _____  ______    __ _ _                                        _
 |  __ \(_)                         |  __ \|  __ \|  ____|  / _(_) |                                      | |
 | |  | |_  __ _ _ __   __ _  ___   | |  | | |__) | |__    | |_ _| | ___    __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __
 | |  | | |/ _` | '_ \ / _` |/ _ \  | |  | |  _  /|  __|   |  _| | |/ _ \  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |__| | | (_| | | | | (_| | (_) | | |__| | | \ \| |      | | | | |  __/ | (_| |  __/ | | |  __/ | | (_| | || (_) | |
 |_____/| |\__,_|_| |_|\__, |\___/  |_____/|_|  \_\_|      |_| |_|_|\___|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|
       _/ |             __/ |                                               __/ |
      |__/             |___/                                               |___/

Django DRF File Generation provides a safe way to write basic files like url.py, serializers.py, admin.py, views.py, based on your models.py

Free software: MIT license
GitHub: https://github.com/AlexandreProenca/drf-gem
Documentation: http://drf-gem.readthedocs.org/


Usage
-----

       Option:
       -m path/my/models.py   required parameter, path to models.py file
       -a or --admin          to create admin.py
       -v or --views          to create views.py
       -u or --urls           to create urls.py
       -s or --serializers    to create serializers.py
       -A or --All            to create urls.py, admin.py, views.py, serializers.py
       -D or --clean          warning!!! this option will remove gem_build directory and all files inside
       -h or --help           to show all options

      Exemples:
      #python drf-gem -a -s -m path/my/models.py
      #python drf-gem -m path/my/models.py --views --serializers
      #python drf-gem -m path/my/models.py --clean
      #python drf-gem -m path/my/models.py --All



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

`drf-gem` was written by `Alexandre Proença <alexandre.proenca@hotmail.com.br>`_.
