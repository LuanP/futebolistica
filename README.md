futebolistica
=============

Software for management of soccer games
-------------

This software is a school project with learning intents only.


Live demo
-------------

http://futebolistica.herokuapp.com


Install
-------------

Clone the repository

`git clone git@github.com:LuanP/futebolistica.git`

Install the `requirements.txt` running

`pip install -r requirements.txt`

Now run `syncdb` on the folder where is the `manage.py` file

`python manage.py syncdb`

Done.

NOTE
----
You can create a superuser during the syncdb and fill the database with data on admin or
create one on hand later with the `shell`.
