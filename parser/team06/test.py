# JSON Mode Test File
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

from storageManager import jsonMode as j

# drop all databases if exists

# create database
j.createDatabase('world')
j.createDatabase('world1')
j.createDatabase('world')
j.dropDatabase('world')
j.showDatabases()
