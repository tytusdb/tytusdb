from Fase1.Sql import Sql
import sys

def inter(statement):
    sql:Sql = Sql()
    sql.run(statement)

if __name__ == '__main__':
    print(sys.version)


    statement  = """ 

--  Manipulacion de datos
 CREATE DATABASE IF NOT EXISTS test
     OWNER = 'root'
     MODE = 1;

 SHOW DATABASES;

 USE test;

 create table tbcalifica
 ( iditem integer primary key,
   item   varchar(150),
   puntos decimal(8,2),
   seccion integer
 );

 insert into tbcalifica values (1,'Funcionalidades básicas',2.0,0);
 insert into tbcalifica values (2,'Funciones Date-Extract',2.0,0);
 insert into tbcalifica values (3,'esto es un prueba moi x',2.0,0);

use test;
SELECT * FROM tbcalifica;
    
    """

    inter(statement)


# from flask import Flask
# from flask_cors import CORS
# from routes.index import init_routes

# app = Flask (__name__)
# CORS(app)

# init_routes(app)

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5000, debug=True)