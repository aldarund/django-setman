==============================
Test Project for django-setman
==============================

``django-setman`` comes with simple test project that made for check how
library works with different Django versions.

Initialization
==============

Bootstrap testproject with::

    $ python testproject/bootstrap.py

Then choose one of available virtual environments (for example, ``env``),
activate it and init database and setman migrations::

    (env)$ python testproject/manage.py syncdb --noinput
    (env)$ python testproject/manage.py migrate --noinput

And finally you can to get pair of oDesk keys and setup it to
``local_settings.py`` module. After, feel free to run development server::

    (env)$ python testproject/manage.py runserver <port>

and check how ``django-setman`` works.

Run tests
=========

For running tests, check that project already bootstrapped. If all ok, just
run standard Django test command::

    (env)$ python testproject/manage.py test core setman

.. note:: We don't need to provide custom test settings module. All necessary
   options setup at ``testproject.settings`` and your ``local_settings``.

If you want to run tests on each of available virtual environments, run::

    $ ./testproject/runcmd.sh test core setman

Also project has **Jenkins** support (via ``django-jenkins`` app). So to run
complete Jenkins tasks, execute::

    (env)$ python testproject/manage.py jenkins

and then check for data in ``reports/`` directory.
