# HelpDesk

Para hacer uso del mvp, crea la base de datos y setealo con python, primero crea la base de datos con mysql y crea el usuario que se muetra en el codigo con los permisos en la misma base de datos
- from app import db
- db.create_all

para crear un usuario necesitaras un user id, en mysql crea ese id
- INSERT INTO user_id (user_id, used, admin) VALUES ('321', 'false', 'yes');
- luego ya puedes interactuar con el app

Para ejecutar la aplicacion
- LASK_APP=app.py flask run

Para ejecutar api, desde root
- python3 -m api_v1.v1.api
