#!/bin/bash

export PYTHONPATH=${PYTHONPATH}:"$(pwd)"
echo $PYTHONPATH

pipenv run $1 $2 $3 $4 $5 $6
