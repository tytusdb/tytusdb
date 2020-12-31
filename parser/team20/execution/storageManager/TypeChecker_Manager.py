import json

TypeChecker_path = "data/json/TypeChecker"


class TypeChecker_Manager:
    def __init__(self, use, databases):
        self.use = use
        self.databases = databases

class database:
    def __init__(self, name: str, mode: int, types: str, tables):
        self.name = name
        self.mode = mode
        self.types = types
        self.tables = tables
        if self.tables == None:
            self.tables = []

class table:
    def __init__(self, name: str, columns):
        self.name = name
        self.columns = columns
        if self.columns == None:
            self.columns = []

class column:
    def __init__(self, name: str, checks):
        self.name = name
        #constraints
        self.type_: str = None
        self.primary_: bool = None
        self.default_: any = None
        self.null_: bool = None
        self.maxlength_: int = None
        self.unique_: bool = None
        #checks
        self.checks = checks
        if self.checks == None:
            self.checks = []

class check:
    def __init__(self, operation: str, value: any):
        self.operation = operation
        self.value = value


def get_TypeChecker_Manager_Aux(json_string: str):

    TypeChecker_Manager_ = TypeChecker_Manager(None, [])

    content_one = json_string
    content_one = str(content_one).replace("'", "\"")
    content_one = str(content_one).replace("True", "true")
    content_one = str(content_one).replace("False", "false")
    jsonObject_one = json.loads(content_one)
    
    #Database Name---------------------------------
    for key_one in jsonObject_one:
        value_one = jsonObject_one[key_one]
        
        if key_one == "USE":
            TypeChecker_Manager_.use = value_one

        else:
            Database = database(key_one, None, None, [])
            TypeChecker_Manager_.databases.append(Database)
    #----------------------------------------------
            #Table Name------------------------------------
            content_two = value_one
            content_two = str(content_two).replace("'", "\"")
            content_two = str(content_two).replace("True", "true")
            content_two = str(content_two).replace("False", "false")
            jsonObject_two = json.loads(content_two)

            for key_two in jsonObject_two:  
                value_two = jsonObject_two[key_two]

                if key_two == "MODE":
                    Database.mode = value_two

                elif key_two == "TYPES":
                    Database.types = value_two

                else:
                    Table = table(key_two, [])
                    Database.tables.append(Table)
            #----------------------------------------------
                    #Column Name------------------------------------
                    content_three = value_two
                    content_three = str(content_three).replace("'", "\"")
                    content_three = str(content_three).replace("True", "true")
                    content_three = str(content_three).replace("False", "false")
                    jsonObject_three = json.loads(content_three)
            
                    for key_three in jsonObject_three:
                        value_three = jsonObject_three[key_three]

                        Column = column(key_three, [])
                        Table.columns.append(Column)
                    #-----------------------------------------------
                        #Constraints and Checks-------------------------
                        content_four = value_three
                        content_four = str(content_four).replace("'", "\"")
                        content_four = str(content_four).replace("True", "true")
                        content_four = str(content_four).replace("False", "false")
                        jsonObject_four = json.loads(content_four)

                        #Constraints------------------------------------
                        try:
                            Column.type_ = jsonObject_four["CONST"]["TYPE"]
                        except Exception as e:
                            i=0#print(e)
                        try:
                            Column.primary_ = jsonObject_four["CONST"]["PRIMARY"]
                        except Exception as e:
                            i=0#print(e)
                        try:
                            Column.default_ = jsonObject_four["CONST"]["DEFAULT"]
                        except Exception as e:
                            i=0#print(e)
                        try:
                            Column.null_ = jsonObject_four["CONST"]["NULL"]
                        except Exception as e:
                            i=0#print(e)
                        try:
                            Column.maxlength_ = jsonObject_four["CONST"]["MAXLENGTH"]
                        except Exception as e:
                            i=0#print(e)
                        try:
                            Column.unique_ = jsonObject_four["CONST"]["UNIQUE"]
                        except Exception as e:
                            i=0#print(e)
                        #-----------------------------------------------
                        
                        #Checks-----------------------------------------
                        try:
                            for entity in jsonObject_four["CHECKS"]:
                                Check = check(entity["OP"], entity["VALUE"])
                                Column.checks.append(Check)
                        except Exception as e:
                            i=0#print(e)
                        #-----------------------------------------------
                        #-----------------------------------------------
    
    return TypeChecker_Manager_


def get_string_json_TypeChecker_Manager(TypeChecker_Manager_: TypeChecker_Manager):

    json_ = ""
    json_ += "{\n"
    json_ += "      \"USE\": \"" + TypeChecker_Manager_.use + "\""
  
    if len(TypeChecker_Manager_.databases)>0:
        json_ += ",\n"
    else:
        json_ += "\n"

    i = 0
    while i < len(TypeChecker_Manager_.databases):
        #database start--------------------------
        json_ += "      \"" + TypeChecker_Manager_.databases[i].name + "\": {\n"
        #----------------------------------------
        
        #Mode------------------------------------
        json_ += "          \"MODE\":" + str(TypeChecker_Manager_.databases[i].mode) + ",\n"
        #----------------------------------------

        #Types-----------------------------------
        json_ += "          \"TYPES\":" + str(TypeChecker_Manager_.databases[i].types)
        if len(TypeChecker_Manager_.databases[i].tables) > 0:
            json_ += ",\n"
        else:
            json_ += "\n"
        #----------------------------------------
        
        j = 0
        while j < len(TypeChecker_Manager_.databases[i].tables):
            #table start+++++++++++++++++++++++++++++
            json_ += "          \"" + TypeChecker_Manager_.databases[i].tables[j].name + "\": {\n"
            #++++++++++++++++++++++++++++++++++++++++

            k = 0
            while k < len(TypeChecker_Manager_.databases[i].tables[j].columns):
                #column start****************************
                json_ += "              \"" + TypeChecker_Manager_.databases[i].tables[j].columns[k].name + "\": {\n"
                #****************************************

                json_ += "                  \"CONST\": {"   
                
                type_ = TypeChecker_Manager_.databases[i].tables[j].columns[k].type_
                primary_ = TypeChecker_Manager_.databases[i].tables[j].columns[k].primary_
                default_ = TypeChecker_Manager_.databases[i].tables[j].columns[k].default_
                null_ = TypeChecker_Manager_.databases[i].tables[j].columns[k].null_
                maxlength_ = TypeChecker_Manager_.databases[i].tables[j].columns[k].maxlength_
                unique_ = TypeChecker_Manager_.databases[i].tables[j].columns[k].unique_
                
                if type_ != None:
                    json_ += "\"TYPE\": \"" + str(type_) + "\""
                if primary_ != None:
                    json_ += ", \"PRIMARY\": " + str(primary_).lower()
                if default_ != None:
                    json_ += ", \"DEFAULT\": \"" + str(default_) + "\""
                if null_ != None:
                    json_ += ", \"NULL\": " + str(null_).lower()
                if maxlength_ != None:
                    json_ += ", \"MAXLENGTH\": " + str(maxlength_)
                if unique_ != None:
                    json_ += ", \"UNIQUE\": " + str(unique_).lower()

                json_ += "},\n"

                #check start=============================
                json_ += "                  \"CHECKS\": [\n"
                #========================================
                m = 0
                while m < len(TypeChecker_Manager_.databases[i].tables[j].columns[k].checks):
                    json_ += "                  { \"OP\": \"" + str(TypeChecker_Manager_.databases[i].tables[j].columns[k].checks[m].operation) + "\", \"VALUE\": "
                    is_int_or_float_ = is_int_or_float(str(TypeChecker_Manager_.databases[i].tables[j].columns[k].checks[m].value))
                    if is_int_or_float_== True:
                        json_ += str(TypeChecker_Manager_.databases[i].tables[j].columns[k].checks[m].value)
                    else:
                        json_ += "\"" + str(TypeChecker_Manager_.databases[i].tables[j].columns[k].checks[m].value) + "\""
                    json_ += "}"
                    if (m+1) < len(TypeChecker_Manager_.databases[i].tables[j].columns[k].checks):
                        json_ += ",\n"
                    else:
                        json_ += "\n"
                    m += 1
                #check end================================
                json_ += "                  ]\n"
                #========================================

                #column end******************************
                json_ += "              }"
                if (k+1) < len(TypeChecker_Manager_.databases[i].tables[j].columns):
                    json_ += ",\n"
                else:
                    json_ += "\n"
                k += 1
                #****************************************

            #table end+++++++++++++++++++++++++++++++
            json_ += "          }"
            if (j+1) < len(TypeChecker_Manager_.databases[i].tables):
                json_ += ",\n"
            else:
                json_ += "\n"
            j += 1
            #++++++++++++++++++++++++++++++++++++++++
        
        #database end----------------------------
        json_ += "      }"
        if (i+1) < len(TypeChecker_Manager_.databases):
            json_ += ",\n"
        else:
            json_ += "\n"
        i += 1
        #----------------------------------------
    
    json_ += "}"
    json_ = str(json_).replace("'", "\"")
    json_ = str(json_).replace("\"[\"", "\"")
    json_ = str(json_).replace("\"]\"", "\"")

    return json_


def is_int_or_float(input_):
    if is_int(input_) == True or is_float(input_) == True:
        return True
    else:
        return False

def is_int(input_):
	try:
		int(input_)
		return True
	except:
		return False

def is_float(input_):
	try:
		float(input_)
		return True
	except:
		return False


def get_TypeChecker_Manager():
    TypeChecker_Manager_ = None
    try:
        f = open(TypeChecker_path, "r")
        content = f.read()
        f.close()
        TypeChecker_Manager_ = get_TypeChecker_Manager_Aux(content)
    except Exception as e:
        i=0#print(e)                
    return TypeChecker_Manager_


def save_TypeChecker_Manager(TypeChecker_Manager_: TypeChecker_Manager):
    successful_operation = False
    try:
        string_json_TypeChecker_Manager = get_string_json_TypeChecker_Manager(TypeChecker_Manager_)
        f = open(TypeChecker_path, "w")
        f.write(string_json_TypeChecker_Manager)
        f.close()
        successful_operation = True
    except Exception as e:
        i=0#print(e)                
    return successful_operation


def get_use(TypeChecker_Manager_: TypeChecker_Manager) -> str:
    use_ = None
    try:
        use_ = TypeChecker_Manager_.use
    except Exception as e:
        i=0#print(e)    
    return use_

def get_database(database_name: str, TypeChecker_Manager_: TypeChecker_Manager) -> database:
    database_ = None
    try:
        i = 0
        while i < len(TypeChecker_Manager_.databases):
            if TypeChecker_Manager_.databases[i].name == database_name:
                database_ = TypeChecker_Manager_.databases[i]
                i = len(TypeChecker_Manager_.databases)
            i += 1
    except Exception as e:
        i=0#print(e)    
    return database_

def get_table(table_name: str, database_: database) -> table:
    table_ = None
    try:
        i = 0
        while i < len(database_.tables):
            if database_.tables[i].name == table_name:
                table_ = database_.tables[i]
                i = len(database_.tables)
            i += 1
    except Exception as e:
        i=0#print(e)    
    return table_

def get_column(column_name: str, table_: table) -> column:
    column_ = None
    try:
        i = 0
        while i < len(table_.columns):
            if table_.columns[i].name == column_name:
                column_ = table_.columns[i]
                i = len(table_.columns)
            i += 1
    except Exception as e:
        i=0#print(e)    
    return column_