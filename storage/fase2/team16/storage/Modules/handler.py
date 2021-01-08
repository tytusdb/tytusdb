# Storage Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


import os
import pickle
import re
import shutil
import csv
import json


class Handler:

    @staticmethod
    def rootinstance() -> list:
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists('./data/mainRoot.dat'):
            f = open('./data/mainRoot.dat', 'wb')
            f.close()
        if os.path.getsize('./data/mainRoot.dat') > 0:
            with open('./data/mainRoot.dat', 'rb') as f:
                return pickle.load(f)
        return []

    @staticmethod
    def rootupdate(databases):
        f = open('./data/mainRoot.dat', 'wb')
        pickle.dump(databases, f)
        f.close()

    @staticmethod
    def invalid(name: str):
        pattern = re.compile("[A-za-z_#áéíóúÁÉÍÓÚ0]+")
        if pattern.fullmatch(name[0]):
            pattern = re.compile("[A-za-záéíóúÁÉÍÓÚ0-9_#$@]+")
            if pattern.fullmatch(name[1:]):
                return False
        return True

    @staticmethod
    def reset():
        if os.path.exists("data"):
            shutil.rmtree("data")
        os.makedirs('data')
        f = open('./data/mainRoot.dat', 'wb')
        f.close()

    @staticmethod
    def writer(name, tuples):
        with open(name + '.csv', mode='w', newline='', encoding="utf-8-sig") as f:
            writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(tuples)

    @staticmethod
    def tableinstance(mode: str, database: str, tableName: str):
        if os.path.getsize('./data/' + mode + '/' + str(database) + '_' + str(tableName) + '.tbl') > 0:
            with open('./data/' + mode + '/' + str(database) + '_' + str(tableName) + '.tbl', 'rb') as f:
                return pickle.load(f)
        else:
            return None

    @staticmethod
    def tableupdate(mode: str, database: str, tableName: str, structure):
        f = open('./data/' + mode + '/' + str(database) + '_' + str(tableName) + '.tbl', 'wb')
        pickle.dump(structure, f)
        f.close()

    @staticmethod
    def rename(mode: str, oldName, newName):
        try:
            os.rename('./data/' + mode + '/' + oldName, './data/' + mode + '/' + newName)
        except:
            print("No se pudo renombrar")

    @staticmethod
    def delete(filename):
        try:
            os.remove(filename)
        except:
            print("No se encontró el archivo")

    @staticmethod
    def modeinstance(mode: str):
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists('./data/' + mode):
            os.makedirs('data/' + mode)

    @staticmethod
    def readcsv(file):
        reader = csv.reader(open(file, "r", encoding="utf-8-sig"), delimiter=",")
        tmp = []
        for element in reader:
            aux = []
            for x in element:
                if x.isdigit():
                    aux.append(int(x))
                elif x.isdecimal():
                    aux.append(float(x))
                else:
                    aux.append(x)
            tmp.append(aux)
        return tmp

    @staticmethod
    def clean(mode):
        if os.path.exists('./data/' + mode):
            if len(os.listdir('./data/' + mode)) == 0:
                shutil.rmtree('./data/' + mode)

    @staticmethod
    def readJSON(database: str, table: str) -> list:
        path = './data/security/' + database + '_' + table + '.json'
        with open(path, 'r', encoding='UTF-8') as f:
            return json.loads(f.read())

    @staticmethod
    def writeJSON(database: str, table: str, blocks):
        path = './data/security/' + database + '_' + table + '.json'
        with open(path, 'w+', encoding='UTF-8') as f:
            json.dump(blocks, f, ensure_ascii=False, indent=3)
