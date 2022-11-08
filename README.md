## How To run the project? 

1. Open cmd to the path where manage.py file exists
3. Run the following Command: py manage.py runserver

In case any change to models file was done you need: 
1. to make migrations to package model changes into individual migration files: py manage.py makemigrations
2. migrate these changes to the database: py manage.py migrate
