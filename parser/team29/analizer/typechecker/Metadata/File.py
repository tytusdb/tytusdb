import json


def exportFile(struct, name):
    with open("./" + name + ".json", "w") as file:
        json.dump(struct, file)
        # print("Save")


def importFile(name):
    try:
        with open("./" + name + ".json", "r") as file:
            databases = json.load(file)
            return databases
    except:
        if name == "Types":
            return {}
        return []