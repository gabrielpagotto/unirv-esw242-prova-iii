#!/bin/bash

# Ativa o ambiente virtual
source /home/site/wwwroot/venv/bin/activate

# Inicia o servidor Gunicorn
exec gunicorn --bind=0.0.0.0 --workers=4 leilao.wsgi
