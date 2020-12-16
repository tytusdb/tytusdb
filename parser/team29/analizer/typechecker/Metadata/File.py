import json


def exportFile(Databases):
    with open("./Databases.json", "w") as file:
        json.dump(Databases, file)
        print("Export")


def importFile():
    with open("./Databases.json", "r") as file:
        databases = json.load(file)
        return databases
