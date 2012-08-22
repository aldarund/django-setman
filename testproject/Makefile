.PHONY: bootstrap clean distclean server test

ENV ?= env
ENV13 = $(ENV)-1.3
ENV14 = $(ENV)-1.4
ENVTRUNK = $(ENV)-trunk

PYTHON = PYTHONPATH=.:.. $(ENV)/bin/python
PYTHON13 = PYTHONPATH=.:.. $(ENV13)/bin/python
PYTHON14 = PYTHONPATH=.:.. $(ENV14)/bin/python
PYTHONTRUNK = PYTHONPATH=.:.. $(ENVTRUNK)/bin/python

DJANGO_RUNSERVER ?= runserver_plus
HOST ?= 0.0.0.0
PORT ?= 4331

bootstrap:
	bootstrap.py -e $(ENV) --copy-virtualenv -C 'cp -n local_settings.py{{.def,}}'

clean:
	find . -name '*.pyc' -delete

distclean: clean
	rm -rf $(ENV) $(ENV13) $(ENV14) $(ENVTRUNK)

server:
	$(PYTHON) manage.py $(DJANGO_RUNSERVER) $(HOST):$(PORT)

test:
	$(PYTHON) manage.py test core setman
	$(PYTHON13) manage.py test core setman
	$(PYTHON14) manage.py test core setman
	$(PYTHONTRUNK) manage.py test core setman
