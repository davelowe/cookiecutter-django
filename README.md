Cookiecutter: Django
====================

My personal Cookiecutter mold for Django. It currently requires the development
version of cookiecutter.

Project Setup
-------------

Use cookiecutter to create the project:

    $ cookiecutter https://github.com/bkonkle/cookiecutter-django.git

From the root project directory:

    $ mkvirtualenv project_name
    $ pip install -r requirements.txt
    $ npm install -g grunt-cli
    $ npm install

At this point, you can fire up runserver. It will fire up Grunt as a child
process to watch JavaScript templates and Less styles, and set up a livereload
server to automatically refresh as you save files.

Config
------

The configuration relies somewhat on environment variables. Add the following
to your $VIRTUALENV/bin/postactivate:

    # Config Vars
    export DEBUG=True
    export DATABASE_URL=postgres://database_user:mypassword@localhost:5432/database_name

This will use the user 'database_user' with 'mypassword' on the 'database_name' database.

Make sure to add the inverse to postdeactivate:

    # Unset config vars
    unset DEBUG
    unset DATABASE_URL

A better way to handle this will be forthcoming.
