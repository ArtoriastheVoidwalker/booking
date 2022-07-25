#!/bin/bash

# ./env/bin/uvicorn app:app --port 8000 --timeout-keep-alive 10000 --env-file dev.env
./env/bin/uvicorn --reload app.main:app --port 9000 --timeout-keep-alive 10000
# ./env/bin/gunicorn -k uvicorn.workers.UvicornWorker app.main:app -b :8000 --timeout 10000
