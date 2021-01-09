# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Andree Avalos
from .modulo_llaves import insert
import csv
def loadCSV(filepath: str, database: str, table: str, tipado):
    try:
        res = []
        import csv
        with open(filepath, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter = ',')
            j = 0
            for row in reader:
                if tipado:
                    i=0
                    for x in row:
                        if tipado[j][i] == bool:
                            if x == 'False':
                                row[i] = bool(1)
                            else:
                                row[i] = bool(0)
                        else:
                            row[i] = tipado[j][i](x)
                        i=i+1
                    j+=1
                res.append(insert(database,table, row))
        return res
    except:
        return []
