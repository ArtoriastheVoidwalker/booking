#!/bin/bash

if [ "$1" == "-h" ]; then
  echo "Scripts list: "
  for entry in `ls scripts/`; do
    echo ${entry%.sh}
  done
  echo ""
  echo "Usage: ./`basename $0` [script_name]"
  exit 0
fi

./scripts/$1.sh
echo "Successful executed"
