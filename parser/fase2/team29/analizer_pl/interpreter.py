from re import S
from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))
from analizer_pl.C3D.operations import block
from analizer_pl.reports import BnfGrammar
from analizer_pl.abstract import global_env
import analizer_pl.grammar as grammar
from analizer_pl.libs import File


def traducir(input):
    result = grammar.parse(input)
    lexerErrors = grammar.returnLexicalErrors()
    syntaxErrors = grammar.returnSyntacticErrors()
    env = global_env.GlobalEnvironment()
    c3d = "from sys import path\n"
    c3d += "from os.path import dirname as dir\n"
    c3d += "path.append(dir(path[0]))\n"
    c3d += "from analizer import interpreter as fase1\n"
    c3d += "from goto import with_goto\n"
    c3d += 'dbtemp = ""\n'
    c3d += "stack = []\n"
    c3d += "\n"
    optimizacion = c3d
    if len(lexerErrors) + len(syntaxErrors) == 0 and result:
        for r in result:
            if r:
                c3d += r.execute(env).value
            else:
                c3d += "Instruccion SQL \n"
    f = open("test-output/c3d.py", "w+")
    f.write(c3d)
    f.close()
    optimizacion += grammar.optimizer_.optimize()
    f = open("test-output/c3dopt.py", "w+")
    f.write(optimizacion)
    f.close()
    semanticErrors = []
    functions = functionsReport(env)
    symbols = symbolReport()
    indexes = indexReport()
    obj = {
        "messages": [],
        "querys": [],
        "lexical": lexerErrors,
        "syntax": syntaxErrors,
        "semantic": semanticErrors,
        "postgres": [],
        "symbols": symbols,
        "functions": functions,
        "indexes": indexes,
    }
    grammar.InitTree()
    BnfGrammar.grammarReport()
    return obj


def symbolReport():
    environments = block.environments
    report = []
    for env in environments:
        envName = env[0]
        env = env[1]
        vars = env.variables
        enc = [["ID", "Tipo", "Fila", "Columna", "Declarada en"]]
        filas = []
        for (key, symbol) in vars.items():
            r = [
                symbol.value,
                symbol.type.name if symbol.type else "UNKNOWN",
                symbol.row,
                symbol.column,
                envName,
            ]
            filas.append(r)
        enc.append(filas)
        report.append(enc)
    environments = list()
    return report


def functionsReport(env):
    rep = [["Tipo", "ID", "Tipo de Retorno", "No. de Parametros"], []]
    for (f, x) in env.functions.items():
        r = []
        r.append(x.type)
        r.append(x.id)
        if x.returnType:
            r.append(x.returnType.name)
        else:
            r.append("NULL")
        r.append(x.params)
        rep[1].append(r)
    return rep


def indexReport():
    index = File.importFile("Index")
    enc = [["Nombre", "Tabla", "Unico", "Metodo", "Columnas"]]
    filas = []
    for (name, Index) in index.items():
        columns = ""
        for column in Index["Columns"]:
            columns += (
                ", " + column["Name"] + " " + column["Order"] + " " + column["Nulls"]
            )
        filas.append(
            [name, Index["Table"], Index["Unique"], Index["Method"], columns[1:]]
        )
    enc.append(filas)
    return enc


# region s
s = """ 

CREATE FUNCTION ValidaRegistros(tabla varchar(50),cantidad integer) RETURNS integer AS $$
DECLARE 
resultado INTEGER; 
retorna   INTEGER;
BEGIN
	if tabla = 'tbProducto' then
	    resultado := (SELECT md5('23') si, puta as sho) ;
    	if cantidad = resultado then
			retorna = 1;
		else 
			retorna = 0;
		end if;
	end if;
	if tabla = 'tbProductoUp' then
	    resultado := (SELECT COUNT(*) FROM tbProducto where estado = 2);
    	if cantidad = resultado then
			retorna = 1;
		else 
			retorna = 0;
		end if;
	end if;
	if tabla = 'tbbodega' then
	    resultado := (SELECT COUNT(*) FROM tbbodega);
    	if cantidad = resultado then
			retorna = 1;
		else 
			retorna = 0;
		end if;
	end if;
RETURN retorna;
END;
$$ LANGUAGE plpgsql;
delete from tbbodega as tb where idbodega = 4 and idbodega = 5;
"""

# endregion
# region s2
s2 = """

CREATE FUNCTION foo(texto text, b boolean) RETURNS text AS $$
BEGIN
update tbbodega set bodega = texto||"fr", id = 1 where idbodega = 4; 
update tbbodega set bodega = "fr" where idbodega = 4; 
return texto;
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION myFuncion(texto text, b boolean) RETURNS text AS $$
BEGIN
INSERT INTO tbProducto values(1,'Laptop Lenovo',md5(texto),1);
SELECT 3-5>4 and -3=texto as sho, texto between symmetric 2 and 3 as alv;

select * from tbCalificacion;
select * from tbventa where ventaregistrada = false;
select * from tbempleadopuesto group by departamento;

select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido;


select v.id+foo(texto, 3)
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido,fechaventa
limit 1;

select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido
UNION
select DISTINCT * 
from tbventa V,tbempleado E
where V.idempleado = texto
group by 1,2,3
order by 1;

b = texto between symmetric 2 and 3;
RETURN (3+1)*-1;
END;
$$ LANGUAGE plpgsql;

select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido;

select (3+3)*5;

select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido
UNION
select DISTINCT * 
from tbventa V,tbempleado E
where V.idempleado = texto
group by 1,2,3
order by col ,1 ;


"""
# endregion

# region s3
s3 = """
select E.* from tabla;
select departamento,count(*) CantEmpleados 
from tbempleadopuesto
group by departamento;
select primernombre,segundonombre,primerapellido,sum(montoventa) 
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido;
create table tblibrosalario
( idempleado integer not null,
  aniocalculo integer not null CONSTRAINT aniosalario CHECK (aniocalculo > 0),
  mescalculo  integer not null CONSTRAINT mescalculo CHECK (mescalculo > 0),
  salariobase  money not null,
  comision     decimal,
  primary key(idempleado)
 );
EXECUTE md5("francisco");
update tbbodega set bodega = 'bodega zona 9' where idbodega = 4; 
update tbbodega set bodega = DEFAULT where idbodega = 4; 
"""

# endregion

# region s4
s4 = """

CREATE FUNCTION ValidaRegistros(tabla varchar(50),cantidad integer) RETURNS integer AS $$
DECLARE resultado INTEGER; 
		retorna   INTEGER;
BEGIN
	if tabla = 'tbProducto' then
	    resultado := not ((4+4*10/3) NOT IN  (SELECT COUNT(*) FROM tbProducto)); 
		retorna = 0;
		
	end if;
	if tabla = 'tbProductoUp' then
	    resultado := xd IN (SELECT * FROM tbProducto where estado = 2);
    	retorna = 1;
	end if;
	if tabla = 'tbbodega' then
	    resultado := EXISTS (SELECT COUNT(*) FROM tbbodega);
    	retorna = 2;
	end if;
RETURN retorna;
END;
$$ LANGUAGE plpgsql;				 
	
"""
# endregion

# region s5
s5 = """
use test;
ALTER TABLE tbusuario
ALTER COLUMN password TYPE varchar(80);
insert into tbusuario
values(
    1,
    'Luis Fernando',
    'Salazar Rodriguez',
    'lsalazar',
    MD5('paswword'),
    now()
  );
insert into tbusuario
values(
    2,
    'Maria Cristina',
    'Lopez Ramirez',
    'mlopez',
    MD5('Diciembre'),
    now()
  );
insert into tbusuario
values(
    3,
    'Hugo Alberto',
    'Huard Ordoñez',
    'hhuard',
    MD5('Rafael'),
    now()
  );
insert into tbusuario
values(
    4,
    'Pedro Peter',
    'Parker',
    'ppeter',
    MD5('Donatelo'),
    now()
  );
insert into tbusuario
values(
    5,
    'Mariana Elizabeth',
    'Zahabedra Lopez',
    'melizabeth',
    MD5('Miguel123'),
    now()
  );
insert into tbusuario
values(
    6,
    'Lisa Maria',
    'Guzman',
    'lmaria',
    MD5('Diciembre$$2020'),
    now()
  );
insert into tbusuario
values(
    7,
    'Aurelio',
    'Baldor',
    'abaldor',
    MD5('Algebra$*'),
    now()
  );
insert into tbusuario
values(
    8,
    'Elizabeth Taylor',
    'Juarez',
    'etaylor',
    MD5('hilbilly'),
    now()
  );
insert into tbusuario
values(
    9,
    'Lois',
    'Lane',
    'llane',
    MD5('smallville'),
    now()
  );
select *
from tbusuario;
insert into tbrolxusuario
values(1, 1);
insert into tbrolxusuario
values(2, 2);
insert into tbrolxusuario
values(2, 3);
insert into tbrolxusuario
values(3, 4);
insert into tbrolxusuario
values(3, 5);
insert into tbrolxusuario
values(3, 6);
insert into tbrolxusuario
values(2, 7);
insert into tbrolxusuario
values(3, 8);
insert into tbrolxusuario
values(2, 9);
select *
from tbrolxusuario;
insert into tbrol
values (4, 'IT');
insert into tbrol
values (5, 'Gerencia');
insert into tbusuario
values(
    10,
    'Duff',
    'Mackagan',
    'dmackagan',
    MD5('sweetchild'),
    now()
  );
insert into tbrolxusuario
values(1, 10);
insert into tbusuario
values(
    11,
    'Carlos',
    'Mendez Chingui',
    'cmendez',
    MD5('niebla@@'),
    now()
  );
insert into tbusuario
values(
    12,
    'Diego',
    'Joachin',
    'omendez',
    MD5('raizanimal'),
    now()
  );
insert into tbusuario
values(
    13,
    'Carlos Mauricio',
    'Ordoñez Toto',
    'cordonez',
    MD5('radioviejo'),
    now()
  );
insert into tbusuario
values(
    14,
    'Fernando',
    'Gonzalez',
    'fgonzalez',
    MD5('1245678$net'),
    now()
  );
insert into tbusuario
values(
    15,
    'Walter',
    'Reynoso Alvarado',
    'wreynoso',
    MD5('corona*virus'),
    now()
  );
insert into tbrolxusuario
values(1, 11);
insert into tbrolxusuario
values(1, 12);
insert into tbrolxusuario
values(1, 13);
select *
from tbrolxusuario;
"""
# endregion

# traducir("SELECT 3+3;")
