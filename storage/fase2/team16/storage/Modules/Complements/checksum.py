# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


import hashlib
import sys
import os

ALGORITMOS = ['MD5', 'SHA256']


def checksum_DB(database: str, mode: str, algorithm: str) -> str:
    sys.path.append("......")
    files = ['data/'+str(mode)+'/'+filename for filename in os.listdir('data/'+str(mode)) if filename.startswith(database+'_')]
    for file in files:
        try:
            f = open(file, "rb")
        except IOError as e:
            print(e)
        else:
            data = f.read()
            f.close()
            if algorithm[0].upper() == 'M':
                h = hashlib.md5()
            else:
                h = hashlib.sha256()
            h.update(data)
    hexdigest = h.hexdigest()
    return hexdigest


def checksum_TBL(database: str, table: str, mode: str, algorithm: str) -> str:
    sys.path.append("......")
    file = 'data/' + str(mode) + '/' + str(database) + '_' + str(table) + '.tbl'
    try:
        f = open(file, "rb")
    except IOError as e:
        print(e)
    else:
        data = f.read()
        f.close()
        if algorithm[0].upper() == 'M':
            h = hashlib.md5()
        else:
            h = hashlib.sha256()
        h.update(data)
    hexdigest = h.hexdigest()
    return hexdigest