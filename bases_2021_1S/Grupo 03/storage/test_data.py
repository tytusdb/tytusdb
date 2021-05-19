from storage.mode import mode as modeType


def test1(modeNumber):
    mode = modeType(modeNumber)

    if mode == None:
        return

    # print(mode.dropAll())

    # create database
    print(mode.createDatabase('world'))
    print(mode.showDatabases())

    # create tables
    print(mode.createTable('world', 'countries', 4))
    print(mode.createTable('world', 'cities',    4))
    print(mode.createTable('world', 'languages', 4))
    print(mode.showTables('world'))

    # create simple primary keys
    print(mode.alterAddPK('world', 'countries', [0]))
    print(mode.alterAddPK('world', 'cities',    [0]))
    print(mode.alterAddPK('world', 'languages', [0, 1]))
    print(mode.showTables('world'))

    # insert data in countries
    print(mode.insert('world', 'countries', [
        'GTM', 'Guatemala',  'Central America', 108889]))
    print(mode.insert('world', 'countries', [
        'SLV', 'El Salvado', 'Central America', 21041]))
    print(mode.extractTable('world', 'countries'))

    # insert data in cities
    print(mode.insert('world', 'cities', [
          1, 'Guatemala',    'Guatemala',    'GTM']))
    print(mode.insert('world', 'cities', [
          2, 'Cuilapa',      'Santa Rosa',   'GTM']))
    print(mode.insert('world', 'cities', [
          3, 'San Salvador', 'San Salvador', 'SLV']))
    print(mode.insert('world', 'cities', [
          4, 'San Miguel', 'San Miguel', 'SLV']))
    print(mode.extractTable('world', 'cities'))

    # inser data in languages
    print(mode.insert('world', 'languages', [
          'GTM', 'Spanish', 'official',  64.7]))
    print(mode.insert('world', 'languages', [
          'SLV', 'Spanish', 'official', 100.0]))
    print(mode.extractTable('world', 'languages'))

    # show all data
    # print(mode.showCollection())


def test2(modeNumber):
    mode = modeType(modeNumber)

    if mode == None:
        return

    print(mode.createDatabase('db1'))      # 0
    print(mode.createDatabase('db4'))      # 0
    print(mode.createDatabase('db1'))      # 2
    print(mode.createDatabase('db5'))      # 0
    print(mode.createDatabase(0))          # 1
    print(mode.alterDatabase('db5', 'db1'))  # 3
    print(mode.alterDatabase('db5', 'db2'))  # 0
    print(mode.dropDatabase('db4'))        # 0
    print(mode.showDatabases())            # ['db1','db2']

    # test Tables CRUD
    print(mode.createTable('db1', 'tb4', 3))     # 0
    print(mode.createTable('db1', 'tb4', 3))     # 3
    print(mode.createTable('db1', 'tb1', 3))     # 0
    print(mode.createTable('db1', 'tb2', 3))     # 0
    print(mode.alterTable('db1', 'tb4', 'tb3'))  # 0
    print(mode.dropTable('db1', 'tb3'))         # 0
    print(mode.alterAddPK('db1', 'tb1', 0))      # 1
    print(mode.alterAddPK('db1', 'tb1', [0]))    # 0
    print(mode.showTables('db1'))              # ['tb1', 'tb2']

    # test Registers CRUD
    print(mode.insert('db1', 'tb1', [1, 1]))              # 5
    print(mode.insert('db1', 'tb1', ['1', 'line', 'one']))   # 0
    print(mode.loadCSV('tb1.csv', 'db1', 'tb1'))         # [0, 0, 0, 0, 0]
    print(mode.extractTable('db1', 'tb1'))
    # [['1', 'line', 'one'], ['2', 'line', 'two'],
    #  ['3', 'line', 'three'], ['4', 'line', 'four'],
    #  ['5', 'line', 'five'], ['6', 'line', 'six']]
