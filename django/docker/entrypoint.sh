#!/usr/bin/env bash


echo "Generating Migrations"
python manage.py makemigrations
echo "Done!"

echo "Migrate..."
python manage.py migrate --noinput
echo "Migrated!"

# echo "Loading fixtures..."
# python manage.py loaddata */fixtures/*.json
# echo "Done!"

python manage.py runserver 0.0.0.0:9000
