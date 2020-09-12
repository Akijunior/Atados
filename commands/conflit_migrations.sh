#!/usr/bin/env bash

# Usar apenas em sistemas de testes, pois deleta todos os dados existentes
# e em cache para efetuar a recriação das tabelas.

python src/manage.py clear_cache
python src/manage.py clean_pyc
python src/manage.py reset_schema
python src/manage.py reset_db

python src/manage.py makemigrations
python src/manage.py migrate