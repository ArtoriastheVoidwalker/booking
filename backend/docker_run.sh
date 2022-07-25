#!/bin/bash


docker run -d -h local --platform linux/amd64 -p 9000:9000 --env-file .env booking-backend:latest