# flask_cities_api

## Install

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the main branch. :

```bash

$ git clone https://github.com/mbrav/flask_cities_api
$ cd flask_cities_api

$ git tag  # shows the tagged versions
$ git checkout latest-tag-found-above
$ cd examples/tutorial
```

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install flask_cities_api::

    $ pip install -e .

Or if you are using the main branch, install Flask from source before
installing flask_cities_api::

    $ pip install -e ../..
    $ pip install -e .

## Run

    $ export FLASK_APP=flask_cities_api
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

Or on Windows cmd::

    > set FLASK_APP=flask_cities_api
    > set FLASK_ENV=development
    > flask init-db
    > flask run

Open http://127.0.0.1:5000 in a browser.

## Test

    $ pip install '.[test]'
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser
