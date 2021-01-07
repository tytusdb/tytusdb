from StoreManager import jsonMode as j

if __name__ == '__main__':

## exp = 1 + 1 +1 +1
	# drop all databases if exists
	j.dropAll()

	# create database
	j.createDatabase('world')

	# create tables
	j.createTable('world', 'countries', 4)
	j.createTable('world', 'cities', 4)
	j.createTable('world', 'languages', 4)

	# create simple primary keys
	j.alterAddPK('world', 'countries', [0])
	j.alterAddPK('world', 'cities', [0])
	j.alterAddPK('world', 'languages', [0, 1])

	'''
		create database world;
		use world;
		
		create table countries(
			acronimo  integer  primary key not null,
			name      varchar(50),
			region    varchar(50),
			code      integer
		);

		'code,0,,0,0,:,::,0,:,'
		'region,2,,0,0,:,::,0,:'
		'name,2,,0,0,:,::,0,:'
		'acronimo,0,,1,0,:,::,1,:'
		
		
		
		insert into countries(acronimo,name)values('AR','Argentina');
	'''

	# insert data in countries
	j.insert('world', 'countries', ['acronimo,0,,1,0,:,::,1,:','name,2,,0,0,:,::,0,:','region,2,,0,0,:,::,0,:', 'code,0,,0,0,:,::,0,:,'])
	j.insert('world', 'countries', ['AR','Argentina','',''])
	j.insert('world', 'countries', ['GTM', 'Guatemala', 'Central America', 108889])
	j.insert('world', 'countries', ['SLV', 'El Salvado', 'Central America', 21041])
	j.insert('world', 'countries', ['MX', 'MEXICO', 'NORTE AMERICA', 210410])

	# insert data in cities
	j.insert('world', 'cities', [1, 'Guatemala', 'Guatemala', 'GTM'])
	j.insert('world', 'cities', [2, 'Cuilapa', 'Santa Rosa', 'GTM'])
	j.insert('world', 'cities', [3, 'San Salvador', 'San Salvador', 'SLV'])
	j.insert('world', 'cities', [4, 'San Miguel', 'San Miguel', 'SLV'])

	# inser data in languages
	j.insert('world', 'languages', ['GTM', 'Spanish', 'official', 64.7])
	j.insert('world', 'languages', ['SLV', 'Spanish', 'official', 100.0])
	a = j.extractTable('world', 'cities')
	print("----------------ESTA ES LA PRUEBA")
	print(a)
	print("----------------ESTA ES LA PRUEBA")
	# update
	j.showCollection()
	j.update('world','cities',{2: 'Brasil'},[3])
	j.update('world', 'cities', {2: 'Brasil'}, [4])
	# show all data
	j.showCollection()

	lis = list()
	lis = j.extractTable('world','countries')
	for item in lis:
		print(item)

	'''

		
		insert into t1 (id, nombre) values (1,'lola');
		
	'''

	#todo:Definir check, evualuar exp con interprete
	'''

		create database dab1;
		use dab1;
		create table t1(
			id INTEGER ,
			nombre VARCHAR (2) check(nombre != 'lola')
			primarykey(id,nombre)
		);

		'nombre,2,,0,0,,check, '
		
		insert into t1 (id, nombre) values (1,'lola');
		
	'''

	'''
		nombre,   						sete el nombre de la columna
		typo,     						setea un tipo de dato en numero 
		default,  						Setea un valor fijo 
		not null, 						Setea si es nulo : acitvado= 1	
	    null,     						Setea si es nulo : activado= 1	
	  	unique:nombre,   				Setea un nombre por default si no biene  base_tabla_columan_unique
	  	foreignkey:nameref:columnref, 	si = 1 no = 0
	  	primarykey,   					si = 1 no = 0
	  	check:expresccion,    aun por definir
	'''
