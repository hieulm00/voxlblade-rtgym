## Create a virtual environment

`python -m venv env`

## Activate the virtual environment (Windows)

`./env/Scripts/activate`

## Install packages

`py -m pip install -r requirements.txt`

## Save packages from environment

`py -m pip freeze > requirements.txt`

## Cleanup

`py -m pip freeze | xargs pip uninstall -y`
