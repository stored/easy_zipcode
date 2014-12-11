OUTPUT_HTML = $(filter-out $@,$(MAKECMDGOALS))

test:
	coverage run --branch --source=django/app  django/app/./manage.py test django/app/ -v 2 --failfast --settings=settings.test
	coverage report --omit=django/app/*/migrations*,django/app/settings/*,django/app/urls.py,django/app/wsgi.py,django/app/manage.py,django/app/*/tests/*,django/app/__init__.py

html:
	coverage html --omit=django/app/*/migrations*,django/app/settings/*,django/app/urls.py,django/app/wsgi.py,django/app/manage.py,django/app/*/tests/*,django/app/__init__.py
	open htmlcov/index.html

doc:
	$(MAKE) -C docs/ html
	open docs/_build/html/index.html

deploy:
	fab -f django/fabfile.py deploy

clean:
	rm -f .coverage
	rm -rf htmlcov/
	rm -rf docs/build/

rmpyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
