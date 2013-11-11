futebolistica
=============

Software for management of soccer games
-------------

This software is a school project with learning purposes only.
Developed with Python + Django gives you the opportunity to create and manage soccer leagues.
Easy to run and with a very simple code.

Feel free to edit, upgrade and send pull requests.


### Live demo

http://futebolistica.herokuapp.com


### Install

#### Prerequisites

* PIL
* Git
* pip

#### Recommended

* virtualenv


Clone the repository

`git clone git@github.com:LuanP/futebolistica.git`

Install the `requirements.txt` running

`pip install -r requirements.txt`

Go to the project folder where the `local_settings_example.py` is located and run

`cp local_settings_example.py local_settings.py`

**WARNING**

> If don't get the `local_settings.py` the default database is `PostgreSQL` and you can check and modify the
> configuration on `settings.py` file. The `local_settings.py` has the `sqlite3` configured and ready to run.

Now run `syncdb` on the folder where is the `manage.py` file

`python manage.py syncdb`

**Done.**

### Note

You can create a superuser during the `syncdb` and fill the database with data on admin or
create one on hand later with the `shell`.
