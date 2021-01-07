
#CREATE A DICTIONARY TO STORE THE SYMBOLS
symbolTable=dict()
#CREATE A NEW SYMBOL AND STORE IT INTO THE SYMBOL TABLE
def add_symbol(name_,type_,value_,row_,column_,ambit_):
    symbolTable[name_]=[type_,value_,row_,column_,ambit_]

#SEARCH A SYMBOL WITH name_ IF IS FOUND, THE RETURN name_, type_ AND value_
def search_symbol(name_):
    if name_ in symbolTable:
        return name_,symbolTable[name_][0],symbolTable[name_][1]
    else:
        return 0
#MODIFY THE VALUE OF A SYMBOL, THE type_ VERIFICATION MUST BE DONE BEFORE EXECUTE THIS
def modify_symbol(name_,value_):
    if name_ in symbolTable:
        symbolTable[name_][1]=value_ 

