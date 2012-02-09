import os
import sys


DIRNAME = os.path.abspath(os.path.dirname(__file__))
rel = lambda *x: os.path.abspath(os.path.join(DIRNAME, *x))

PROJECT_DIR = rel('..')
activate_this = rel('env', 'bin', 'activate_this.py')

# Activate virtualenv
execfile(activate_this, {'__file__': activate_this})

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
os.environ['PYTHON_EGG_CACHE'] = '/srv/python_eggs/'

# Need to add upper-level dir to syspath to reproduce dev Django environ
sys.path.append(PROJECT_DIR)

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
