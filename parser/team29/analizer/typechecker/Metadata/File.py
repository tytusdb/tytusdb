import json

def exportFile(Databases,name):
    with open('parser/team29/TypeChecker/Metadata/'+name+'.json','w') as file:
        json.dump(Databases,file)
        print("Export")

def importFile(name):
    with open('parser/team29/TypeChecker/Metadata/'+name+'.json','r') as file:
        databases = json.load(file)
        return databases
        