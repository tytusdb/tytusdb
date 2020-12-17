from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from analizer import grammar

s = """ 
    --SELECT padres.parent as p, padres.child from parents as padres;
    --SELECT name, phone, location from company, users;
    --SELECT 9+8!=8+9 or 8*8 != 64;
    --SELECT 9+8!=8+9 and 8*8 = 64;
    --SHOW DATABASES;
    --USE DATABASE db1;
    --INSERT INTO company VALUES (2, "Pillofon", 3200);
    --USE DATABASE db5;
    --INSERT INTO company VALUES (2, "Microsoft", 8080);
    --CREATE DATABASE db1;
    
    USE DATABASE db1;
    /*
    CREATE TABLE Usuario2(
        dpi bigint not null primary key,
        socio bigint not null,
        saldo money DEFAULT 1000,
        nombre varchar(30),
        fecha date,
        dias interval day,
        unique (dpi,saldo,nombre),
        primary key (dpi,nombre),
        FOREIGN key (socio) REFERENCES prueba1 (dpi)
    );
    

    SELECT customer.first_name as nombre, purchase.amount as amount, product.name as producto, product.price as precio
    WHERE amount < 10 AND purchase.cust_id=customer.id AND purchase.prod_id=product.id;
*/
    SELECT 9+8!=8+9 or 8*8 != 64 AND 9+8!=8+9 or 8*8 = 64 IS TRUE as XD;

    SELECT date_part('days', NOW()), CURRENT_TIME, EXTRACT(month FROM TIMESTAMP 'now');
    SELECT NOW();
    
    --INSERT INTO Usuario VALUES (3216883330506, 100000, "Francisco Suarez", "1999-08-16 10:28:30", 5);
"""

result = grammar.parse(s)
print(result)
