#!/bin/bash

heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python
heroku config:set PYTHON_RUNTIME_VERSION=3.8.10
heroku config:set POETRY_VERSION=1.1.8
# Run pipeline tests
heroku config:set POETRY_EXPORT_DEV_REQUIREMENTS=1
# Disable creation of runtime.txt
#heroku config:set DISABLE_POETRY_CREATE_RUNTIME_FILE=1

