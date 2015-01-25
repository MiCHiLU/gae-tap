[![Build Status](https://travis-ci.org/MiCHiLU/gae-tap.svg?branch=master)](https://travis-ci.org/MiCHiLU/gae-tap)
[![wercker status](https://app.wercker.com/status/72878e11dca6d30f174e95253d766075/s/master "wercker status")](https://app.wercker.com/project/bykey/72878e11dca6d30f174e95253d766075)
[![Code Health](https://landscape.io/github/MiCHiLU/gae-tap/master/landscape.svg)](https://landscape.io/github/MiCHiLU/gae-tap/master)

# A full stack framework for the Google App Engine -based

Let's finish the work quickly and go TAP BEER!

![Man's Beautiful Creation by Idoknow19, on Flickr](http://farm5.staticflickr.com/4114/4809856899_e889084816.jpg)

Looking for sponsors:

1. [$120 - I will get 30L barrel beer!!!](https://www.gittip.com/MiCHiLU/)
2. [ $60 - I will get 15L barrel beer!! ](https://www.gittip.com/MiCHiLU/)
3. [ $12 - I will get  1   pint  beer!  ](https://www.gittip.com/MiCHiLU/)
4. [  $6 - I will get 1/2  pint  beer!  ](https://www.gittip.com/MiCHiLU/)

## Status

* [Travis CI](https://travis-ci.org/MiCHiLU/gae-tap)
* [Wercker CI](https://app.wercker.com/project/bykey/72878e11dca6d30f174e95253d766075)
* [Code Health](https://landscape.io/github/MiCHiLU/gae-tap/master)

## Features

Supports:

* [Google App Engine / Python 2.7](https://cloud.google.com/appengine/docs/python/)
  * [Google Cloud Endpoints API](https://cloud.google.com/appengine/docs/python/endpoints/)
  * [NDB Asynchronous Operation](https://cloud.google.com/appengine/docs/python/ndb/async)
    * [Python NDB Datastore API](https://cloud.google.com/appengine/docs/python/ndb/)
  * [Python Module Configuration](https://cloud.google.com/appengine/docs/python/tools/appengineconfig)
* [Google Analytics for feature phone](https://github.com/MiCHiLU/Google-Analytics-for-Mobile--Google-App-Engine)
* I18N / Python, HTML and JavaScript / [babel](http://babel.pocoo.org/)
* Japanese han-kaku characters / 半角 / [zenhan-py](https://github.com/MiCHiLU/zenhan-py)
* OAuth login / [gae-simpleauth](https://github.com/MiCHiLU/simpleauth)
* [Google OAuth 2.0](https://developers.google.com/accounts/docs/OAuth2) authentication-based Users API (alternate of [Google App Engine Users API](https://cloud.google.com/appengine/docs/python/users/))
* generating sitemaps
* [sessions](https://webapp-improved.appspot.com/api/webapp2_extras/sessions.html)
* Google Cloud Endpoints API as a CRUD, avoid method naming conflict in implemented with multiple classes
* [Endpoints Proto Datastore API](https://github.com/GoogleCloudPlatform/endpoints-proto-datastore)

Low cost operating:

* Google Drive Spreadsheets as a database via Google Visualization API
* Google Drive Form-based feedback system
* hosting as a proxy
  * DropBox
  * Google Drive
* hostname-based multitenancy
  * supports robots.txt
* just a few costs permanent caching and key-value store via taskqueue API
* minimum OAuth accounting
* redirecting to Google URL Shortener

Performance:

* pre-compiling jinja2 templates to Python byte code / [jinja2precompiler](https://github.com/MiCHiLU/jinja2-precompiler)
* [uglify-js](https://github.com/mishoo/UglifyJS)

Coding:

* [CoffeeScript](http://coffeescript.org/)
* [HAML](http://haml.info/)
* [SASS](http://sass-lang.com/) / [compass](http://compass-style.org/)

Development:

* [AngularJS](https://angularjs.org/)
* [Appstats](https://cloud.google.com/appengine/docs/python/tools/appstats)
* [Jinja2 2.6](http://jinja.pocoo.org/docs/dev/)
* [Twitter bootstrap](http://getbootstrap.com/)
* [webapp2](https://cloud.google.com/appengine/docs/python/tools/webapp2)

* [file system event-based automation building on Mac OS X 10.7+](https://pypi.python.org/pypi/watchlion)
* [Docker](https://www.docker.com/)

Testing:

* [py.test](http://pytest.org/)
* coverage of tests / [pytest-cov](https://pypi.python.org/pypi/pytest-cov)
* [karma](http://karma-runner.github.io/)

Utils:

* CORS
* CSRF guard
* HMAC
* e-mail reports of errors
* fanstatic
* handling taskqueue
* managing cache records
* memoize
* ring buffer
* token bucket

Continuous Integration Supports:

* [Travis CI](https://travis-ci.org/)
* [Wercker CI](http://wercker.com/)

## Set up

    $ git clone https://github.com/MiCHiLU/gae-tap.git
    $ cd gae-tap
    $ bundle install
    $ npm install
    $ mkvirtualenv --python=`which ptyhon2.7` gae-tap
    (gae-tap)$ pip install -r requirements.txt
    (gae-tap)$ pip install -r requirements-gae.txt

## Set environ

It need the `GOOGLE_APPENGINE` environ args. Default `GOOGLE_APPENGINE` as below:

    GOOGLE_APPENGINE=$HOME/google-cloud-sdk/platform/google_appengine

If you want to set other path, define `GOOGLE_APPENGINE` in environ as below:

    $ GOOGLE_APPENGINE=<path to your gae> make

## Docker

or, Quickly set up environment via Docker:

    $ docker pull michilu/gae-tap

## First time build

First, you must be build core library:

    (gae-tap)$ (cd gae/tap && make release)

Or, update core library from releases:

1. Download `gaetap-<release-number>.zip` file from https://github.com/MiCHiLU/gae-tap/releases
2. Then replace with files and directories in your repository.

If you want to start a new project with `make scaffold`, as below:

    $ make scaffold
    your app-id, default 'gae-tap': <type your app-id>
    your github user name, default 'MiCHiLU': <type your github user name>

## Build and Test

    (gae-tap)$ make

## Run development server

    (gae-tap)$ make runserver

then access to:

* admin server: [http://localhost:8000](http://localhost:8000)
* instance server: [http://localhost:8080](http://localhost:8080)

## Deploy

    (gae-tap)$ make deploy

Auto deploy via Wercker CI:

If you want to auto deploy to the Google App Engine, add `APP_ENGINE_EMAIL` and `APP_ENGINE_PASSWORD` variables to `Deploy pipeline` of `Deploy targets` in your `App` on the Wercker CI.

## Dependencies

* [Bundler](http://bundler.io/)
* GNU Make
  * [How to install Xcode Command Line Tools](http://railsapps.github.io/xcode-command-line-tools.html)
* Python 2.7
  * [Third-party Libraries in Python 2.7](https://cloud.google.com/appengine/docs/python/tools/libraries27) on Google App Engine
* [npm](https://www.npmjs.com/)

## LICENSE

Licensed under the terms of the MIT.

Copyright (c) 2013 ENDOH takanao