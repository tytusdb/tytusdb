import os 
import json

path = 'data/type/'
dataPath = path + 'typeEnum.json'

#Stuff
def insertEnum(name: str, enum: list) -> bool:
    try:
        if enumExist(name):
            raise Exception
        initCheck()
        data = read(dataPath)
        data[name] = enum
        write(dataPath, data)
        return True
    except:
        return False

def getEnum(name: str) -> list:
    try:
        if not name.isidentifier():
            raise Exception()
        initCheck()
        data = read(dataPath)
        if not name in data:
            raise Exception()
        return data[name]
    except:
        return None

def enumExist(name: str) -> bool:
    try:
        if not name.isidentifier():
            raise Exception()
        initCheck()
        if not name in read(dataPath):
            raise Exception()
        return True
    except:
        return False

# Utilities
def initCheck():
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('data/type'):
        os.makedirs('data/type')
    if not os.path.exists('data/type/typeEnum.json'):
        data = {}
        with open('data/type/typeEnum.json', 'w') as file:
            json.dump(data, file)

# Read a JSON file
def read(path: str) -> dict:
    with open(path) as file:
        return json.load(file)    

# Write a JSON file
def write(path: str, data: dict):
    with open(path, 'w') as file:
        json.dump(data, file)

# Delete all databases and tables by creating a new file
def dropAll():
    initCheck()
    data = {}
    with open('data/type/typeEnum', 'w') as file:
        json.dump(data, file)
