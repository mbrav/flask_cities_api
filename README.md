# flask_cities_api

Flask Microservice API for finding towns and cities

By default, the app loads 1117 cities and their respective 85 regions in Russia that was scraped from a [table from Wikipedia](https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8).

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

```bash
$ python run.py
```

Open http://127.0.0.1:5000 in a browser.
