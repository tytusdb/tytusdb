# Storage Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


import os
import pickle
import re
import shutil
import csv


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
        pattern = re.compile("[A-za-z_#]+")
        if pattern.fullmatch(name[0]):
            pattern = re.compile("[A-za-z0-9_#$@]+")
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
        with open(name + '.csv', mode='w', newline='') as f:
            writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(tuples)

    @staticmethod
    def delete(filename):
        try:
            os.remove(filename)
        except:
            print("No se encontró el archivo")
