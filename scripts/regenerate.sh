#!/bin/bash

echo "-> Remove cinemair DB"
dropdb cinemair
echo "-> Create cinemair DB"
createdb cinemair

echo "-> Load migrations"
python manage.py migrate

echo "-> Load sample-data"
python manage.py sampledata
