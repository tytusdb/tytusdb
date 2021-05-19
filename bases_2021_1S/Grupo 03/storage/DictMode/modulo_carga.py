# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Andree Avalos
from modulo_llaves import insert
import csv
def loadCSV(filepath: str, database: str, table: str):
    try:
        res = []
        import csv
        with open(filepath, 'r') as file:
            reader = csv.reader(file, delimiter = ',')
            for row in reader:
                res.append(insert(database,table, row))
        return res
    except:
        return []
