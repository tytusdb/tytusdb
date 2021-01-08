# Storage Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


import hashlib
import os

algorithms = ['MD5', 'SHA256']


def checksum_DB(database: str, mode: str, algorithm: str) -> str:
    files = ['data/' + mode + '/' + filename for filename in os.listdir('data/' + mode) if
             filename.startswith(database + '_')]
    h = hashlib.md5() if algorithm == algorithms[0] else hashlib.sha256()
    h.update(database.encode('utf8'))
    for file in files:
        try:
            f = open(file, "rb")
        except IOError as e:
            print(e)
        else:
            data = f.read()
            f.close()
            h.update(data)
    return h.hexdigest()


def checksum_TBL(database: str, table: str, mode: str, algorithm: str) -> str:
    file = 'data/' + mode + '/' + database + '_' + table + '.tbl'
    h = hashlib.md5() if algorithm == algorithms[0] else hashlib.sha256()
    try:
        f = open(file, "rb")
    except IOError as e:
        print(e)
    else:
        data = f.read()
        f.close()
        h.update(data)
    return h.hexdigest()
