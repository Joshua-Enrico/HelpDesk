# HelpDesk

desde mysql
- create database HelpDesk;
- CREATE USER 'Helpdesk'@'localhost' IDENTIFIED BY 'Helpdesk';
- 
- grant usage on *.* to 'Helpdesk'@'localhost';
- grant all privileges on HelpDesk.* to 'Helpdesk'@'localhost';

Para hacer uso del mvp, crea la base de datos y setealo con python, primero crea la base de datos con mysql y crea el usuario que se muetra en el codigo con los permisos en la misma base de datos, desde el directorio web_dynamic
- from Class import db
- db.create_all


para crear un usuario necesitaras un user id, en mysql crea ese id
- USE HelpDesk;
- INSERT INTO workers_ids (user_id, used, admin) VALUES ('321', 'false', 'yes');
- luego ya puedes interactuar con el app


Para ejecutar la aplicacion desde el directorio web_dynamic
- FLASK_APP=app.py flask run --host=0.0.0.0 --port=5000

Para ejecutar api, desde root
- python3 -m api.v1.api
