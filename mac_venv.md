## Using a Virtual Environment (venv) on a Mac

If you're on a mac, used brew to install python, and are still having an issue installing the `requests` package even via brew, then this alternative using a virtual environment can help:

`python3 -m venv .venv`
`source .venv/bin/activate`
`python -m pip install requests`

You can verify with:

`python -c "import requests; print(requests.__version__)"`

To exit the virtual environment just type:

`deactivate`

#### More general details here
- https://python.land/virtual-environments/virtualenv