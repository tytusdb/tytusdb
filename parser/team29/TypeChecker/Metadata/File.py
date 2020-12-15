import json

def updateFile(Databases):
    dbTemp = importFile()
    for db in dbTemp:
        Databases.append(db)

    with open('Databases.json','w') as file:
        json.dump(Databases,file)
        print("Update")

def exportFile(Databases):
    with open('Databases.json','w') as file:
        json.dump(Databases,file)
        print("Export")

def importFile():
    with open('Databases.json','r') as file:
        databases = json.load(file)
        return databases
        
