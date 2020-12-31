# JSON Mode Test File
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

from StoreManager import jsonMode as j

if __name__ == '__main__':

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

    # insert data in countries
    j.insert('world', 'countries', ['ACRONIMO,pkey,check', 'NOMBRE', 'REGION', 'CODIGO'])
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
        create database dab1;
        use dab1;
        create table t1(
            id INTEGER,
            nombre VARCHAR (2)
        );
        insert into t1 (id, nombre) values (1,'yo');
        
    '''