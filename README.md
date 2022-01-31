# flask_cities_api

Flask Microservice API for finding towns and cities

## Install

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the main branch. :

```bash

$ git clone https://github.com/mbrav/flask_cities_api
$ cd flask_cities_api
```

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Install flask_cities_api::

    $ poetry install .

## Run

    $ export FLASK_APP=flask_cities_api
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

Open http://127.0.0.1:5000 in a browser.
