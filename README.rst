===========
Django-hice
===========

Django-hice is a Django-powered web front-end for the `Horn-ICE Verification Toolkit <https://doi.org/10.1145/3276501>`__.

============
Requirements
============

* `Django <https://www.djangoproject.com/>`__ (2.2.0+)
* `RQ <https://github.com/nvie/rq>`__ (0.13.0+), which builds upon `Redis <https://redis.io/>`__ (3.0.0+)
* `django-rq <https://github.com/rq/django-rq>`__ (1.3.0+)
* The `Horn-ICE Verification Toolkit <https://github.com/horn-ice/hice-dt>`__ (including Sorcar)

============
Installation
============

* Install ``django-hice``:

  .. code-block:: console

    pip install django-hice-1.0.tar.gz

  See the section on distribution for information on how to generate a source distribution.
  Alternatively, you may simply clone the repository into the root directory of your Django project.

* Add ``django_rq`` and ``django_hice`` to ``INSTALLED_APPS`` in your site's ``settings.py``:

  .. code-block:: python

    INSTALLED_APPS = [
        # other apps
        'django_rq',
        'django_hice',
    ]

* Configure (i.e., add) a queue with name ``hice`` in your site's ``settings.py``:

  .. code-block:: python

    RQ_QUEUES = {
        'hice': {
            'HOST': 'localhost',
            'PORT': 6379,
            'DB': 0,
            'DEFAULT_TIMEOUT': 60,
        },
    }

* Configure (i.e., add) ``django-hice``'s custom exception handler in your site's ``settings.py``:

  .. code-block:: python

    RQ_EXCEPTION_HANDLERS = [
        'django_hice.rq_exception_handler.job_exception_handler'
    ]

* Configure (i.e., add) the path to Boogie's binaries in your site's ``settings.py``:

  .. code-block:: python

    BOOGIE_PATH = 'path to Boogie'

* Include ``django_hice.urls`` in your site's ``urls.py``:

  .. code-block:: python

    # Django >= 2.0
    urlpatterns += [
        path('hice/', include('django_hice.urls'))
    ]
    
  You might need to import ``path`` and ``include`` from ``django.urls``.

=====
Usage
=====

1. Set up database for ``django-hice``:

  .. code-block:: console

    python ./manage.py makemigrations django_hice
    python ./manage.py migrate
    
2. Create one (or more) ``django-rq`` workers:

  .. code-block:: console

    python ./manage.py rqworker hice

3. Run a webserver:

  .. code-block:: console
  
    python ./manage.py runserver
  
  and visit http://127.0.0.1:8000/hice/.
  
  Remember to never use Django's development server in a production environment.

============
Distribution
============

``django-hice`` uses ``setuptools`` to allow a simple distribution.

To create a source distribution (which can by installed with ``pip``), use the following command:

  .. code-block:: console

    python setup.py sdist

Refer to the `documentation of setuptools <https://setuptools.readthedocs.io/en/latest/>`__ for more information.