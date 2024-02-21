#!/usr/bin/env bash
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
poetry install

# Convert static asset files
python3 hexlet-code/manage.py collectstatic --no-input

# Apply any outstanding database migrations
python3 hexlet-code/manage.py migrate