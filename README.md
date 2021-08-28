# nt-redaction-back-end

[Project board](https://github.com/NathOrmond/nt-redaction-back-end/projects/2)

The dependencies for this project are managed using poetry. 
- [Introduction to poetry](https://python-poetry.org/docs/)
  
To install poetry on osx or linux run:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

There's more installation options in the docs linked above.

Once installed you can easily install all the dependencies from the lock file. Run
```
poetry install
```
ps. don't push the lock file to the repo.

To add a new dependency (eg: flask), run:
```
poetry add flask
```

It's best to run python files in this repo from a poetry shell:
```
poetry shell
```
then (eg api), 
```
python api/api.py
```
You don't need to specify the python version because that's already managed by poetry!

