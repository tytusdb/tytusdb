CREATE INDEX indice1 ON tablita1 (id_1, id_2 , id_3 , id_4);
CREATE INDEX indice2 ON tablita1 (id_2, id_2);
CREATE INDEX indice3 ON tablita1 (id_3 , id_4);
CREATE INDEX indice4 ON tabla3 USING hash (colum3);
CREATE INDEX indice4 ON tabla3 USING hash (colum3);

ALTER INDEX indice1 ALTER COLUMN id_2 idcambio ;
ALTER INDEX indice2 ALTER   id_2 cambio2 ;
