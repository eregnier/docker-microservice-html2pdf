dev:
	./venv/bin/flask run --port 8030

run:
	./venv/bin/gunicorn --bind 0.0.0.0:8030 --workers 1 --threads 2 wsgi:app

install: clear
	virtualenv venv -p $(shell which python3)
	./venv/bin/pip install -r requirements.txt

clear:
	rm -rf venv
