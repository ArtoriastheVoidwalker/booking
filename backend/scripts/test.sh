#!/bin/bash

./env/bin/pytest --cov=app --cov-report=term-missing app/tests "${@}"