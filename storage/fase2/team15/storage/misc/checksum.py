# -------------------------------
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

import hashlib
from storage import TytusStorage as h

def checksumDatabase(database, mode):
    try:
        temp=""
        if h._database(database):
            temp += "[-"+database+"-]:"
            if h.showTables(database):
                for i in h.showTables(database):
                    temp += "["+i+"]:"
                    if h.extractTable(database,i):
                        for j in h.extractTable(database,i):
                            if j:
                                for k in j:
                                    temp += str(k) + ","
                    else:
                        temp+="None,"

            else:
                return None

            if temp:
                if mode == "MD5":
                    hash = hashlib.md5(temp.encode(h._database(database)["encoding"])).hexdigest()
                    return hash

                elif mode == "SHA256":
                    hash = hashlib.sha256(temp.encode(h._database(database)["encoding"])).hexdigest()
                    return hash

                else:
                    return None #return 3
            else:
                return None

        else:
            return None #return 2

    except:
        return None #return 1

def checksumTable(database, table, mode):
    try:
        temp = ""
        if h._database(database):
            temp += "[-" + database + "-]:"
            for i in h.showTables(database):
                if i == table:
                    temp += "[-" + i + "-]:"
                    if h.extractTable(database, i):
                        for j in h.extractTable(database, i):
                            for k in j:
                                temp += str(k)+","

                    else:
                        temp+="None"


            if mode == "MD5":
                hash = hashlib.md5(temp.encode(h._database(database)["encoding"])).hexdigest()
                return hash

            elif mode == "SHA256":
                hash = hashlib.sha256(temp.encode(h._database(database)["encoding"])).hexdigest()
                return hash

            else:
                return None

        else:
            return None

    except:
        return None




