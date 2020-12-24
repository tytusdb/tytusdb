# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


import csv
import os
import pickle
import re
import shutil


class Handler:

    # Databases
    @staticmethod
    def rootinstance() -> list:
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists('data/root.dat'):
            f = open('data/root.dat', 'wb')
            f.close()
        if os.path.getsize('data/root.dat') > 0:
            with open('data/root.dat', 'rb') as f:
                return pickle.load(f)
        return []

    @staticmethod
    def rootupdate(databases):
        f = open('data/root.dat', 'wb')
        pickle.dump(databases, f)
        f.close()

    # Tables
    @staticmethod
    def tableinstance(database: str, tableName: str):
        if os.path.getsize('data/' + str(database) + '_' + str(tableName) + '.tbl') > 0:
            with open('data/' + str(database) + '_' + str(tableName) + '.tbl', 'rb') as f:
                return pickle.load(f)
        else:
            return None

    @staticmethod
    def tableupdate(table):
        f = open('data/' + str(table.database) + '_' + str(table.name) + '.tbl', 'wb')
        pickle.dump(table, f)
        f.close()

    @staticmethod
    def exists(database: str, tableName: str):
        return os.path.isfile('data/' + str(database) + '_' + str(tableName) + '.tbl')

    @staticmethod
    def delete(filename):
        try:
            os.remove('data/' + filename)
        except:
            print("No se encontró el archivo")

    @staticmethod
    def rename(oldName, newName):
        try:
            os.rename('data/' + oldName, 'data/' + newName)
        except:
            print("No se pudo renombrar")

    @staticmethod
    def findCoincidences(database, tablesName):
        tmp = []
        for i in tablesName:
            try:
                if os.path.isfile('data/' + str(database) + '_' + str(i) + '.tbl'):
                    tmp.append(str(i))
            except:
                continue
        return tmp

    @staticmethod
    def readcsv(file):
        return csv.reader(open(file, "r"), delimiter=",")

    @staticmethod
    def invalid(name: str):
        pattern = re.compile("[A-za-z_#]+")
        if pattern.fullmatch(name[0]):
            pattern = re.compile("[A-za-z0-9_#$@]+")
            if pattern.fullmatch(name[1:]):
                return False
        return True

    @staticmethod
    def reset():
        shutil.rmtree("data")
        os.makedirs('data')
        f = open('data/root.dat', 'wb')
        f.close()
        if os.path.exists("DataAccessLayer/imaging"):
            shutil.rmtree("DataAccessLayer/imaging")

    # Reports
    @staticmethod
    def init_DirReports():
        if not os.path.exists("DataAccessLayer/imaging"):
            os.makedirs("DataAccessLayer/imaging")
