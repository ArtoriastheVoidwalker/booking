#!/bin/bash


python3 -m venv env
./env/bin/pip3 install --upgrade pip
./env/bin/pip3 install -r requirements.txt --use-feature=2020-resolver
cp dev.env .env
createdb booking
./env/bin/alembic upgrade head
echo "Successful prepared app"
