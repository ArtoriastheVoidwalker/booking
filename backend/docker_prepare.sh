#!/bin/bash


docker build -f develop.dockerfile -t booking-backend .
createdb booking
./env/bin/alembic upgrade head
cp dev.env .env
echo "Successful prepared docker image"
