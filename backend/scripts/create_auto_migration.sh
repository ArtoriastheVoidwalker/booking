#!/bin/bash

set -e
set -x

./env/bin/alembic revision --autogenerate -m "$1"