# Virtual environment
## Create a virtual environment
`python -m venv .env`
## Activate the virtual environment (Windows)
`./.env/Scripts/activate`
## Install packages
`py -m pip install -r requirements.txt`
## Module to get windows from Windows
`py -m pip install pywin32`
## After installing a new package, save packages from environment
`py -m pip freeze > requirements.txt`
## Cleanup
`py -m pip freeze | xargs pip uninstall -y`
