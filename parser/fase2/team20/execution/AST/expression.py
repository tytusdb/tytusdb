from io import StringIO  # Python3
import sys
import inspect

class Expression:
    ''' '''


class Value(Expression):
    types = {
        1: 'Entero',
        2: 'Decimal',
        3: 'Cadena',
        4: 'Variable',
        5: 'Regex',
        6: 'All'
    }
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        v=str(self.value)
        if self.type == 3:v="'"+str(self.value)+"'"
        if self.type==1:
            v=int(str(self.value))
        elif self.type==2:
            v=float(str(self.value))
        return "Value("+str(self.type)+","+str(v)+")"
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        if(self.types[self.type]!='Cadena'): dot += str(hash(self)) + '[label=\"' + str(self.value) + '\"]\n'
        else: dot += str(hash(self)) + '[label=\"\'' + str(self.value) + '\'\"]\n'
        return dot
    def translate(self,opts,indent):
        # diccionario = None
        # if(self.type == 3):
        #     diccionario = {'resultado':opts.generateTemp(),'argumento1':"'"+str(self.value)+"'",'argumento2':None,'operacion':None}
        #     opts.pila.append(diccionario)
        #     return (indent*"\t")+diccionario['resultado']+"='"+str(self.value)+"'\n"
        # diccionario = {'resultado':opts.generateTemp(),'argumento1':str(self.value),'argumento2':None,'operacion':None}
        # opts.pila.append(diccionario)
        # return (indent*"\t")+diccionario['resultado']+"="+str(self.value)+"\n"
        if self.type == 3: self.value = "'"+self.value+"'"
        return self

class Arithmetic(Expression):
    def __init__(self, value1, value2, type):
        self.value1 = value1
        self.value2 = value2
        self.type = type
    def __repr__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.value1)
        val1 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.value2)
        val2 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        return "Arithmetic("+val1+","+val2+",'"+str(self.type)+"')"
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"' + str(self.type) + '\"]\n'
        dot += self.value1.graphAST('',hash(self))
        dot += self.value2.graphAST('',hash(self))
        return dot
    def translate(self,opts,indent):
        t1 = self.value1.translate(opts,indent)
        t2 = self.value2.translate(opts,indent)
        code = ""
        diccionario = {}
        diccionario['resultado']=opts.generateTemp()
        if isinstance(t1,Value): 
            diccionario['argumento1']=str(t1.value)
        else: 
            diccionario['argumento1']=inspect.cleandoc(t1.split("\n")[-2].split("=")[0])
            code+=t1
        if isinstance(t2,Value): 
            diccionario['argumento2']=str(t2.value)
        else: 
            diccionario['argumento2']=inspect.cleandoc(t2.split("\n")[-2].split("=")[0])
            code+=t2
        diccionario['operacion']=self.type
        opts.pila.append(diccionario)
        return code+(indent*"\t")+diccionario['resultado']+"="+diccionario['argumento1']+self.type+diccionario['argumento2']+"\n"

class Range(Expression):
    def __init__(self, value1, value2, type):
        self.value1 = value1
        self.value2 = value2
        self.type = type
    def __repr__(self):    
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.value1)
        val1 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.value2)
        val2 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        return "Range("+val1+","+val2+",'"+str(self.type)+"')"
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"' + str(self.type) + '\"]\n'
        dot += self.value1.graphAST('',hash(self))
        dot += self.value2.graphAST('',hash(self))
        return dot
    def translate(self,opts,indent):
        t1 = self.value1.translate(opts,indent)
        t2 = self.value2.translate(opts,indent)
        code = ""
        diccionario = {}
        diccionario['resultado']=opts.generateTemp()
        if isinstance(t1,Value): 
            diccionario['argumento1']=str(t1.value)
        else: 
            diccionario['argumento1']=inspect.cleandoc(t1.split("\n")[-2].split("=")[0])
            code+=t1
        if isinstance(t2,Value): 
            diccionario['argumento2']=str(t2.value)
        else: 
            diccionario['argumento2']=inspect.cleandoc(t2.split("\n")[-2].split("=")[0])
            code+=t2
        diccionario['operacion']=self.type
        opts.pila.append(diccionario)
        return code+(indent*"\t")+diccionario['resultado']+"="+diccionario['argumento1']+self.type+diccionario['argumento2']+"\n"

class Logical(Expression):
    def __init__(self, value1, value2, type):
        self.value1 = value1
        self.value2 = value2
        self.type = type
    def __repr__(self):    
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.value1)
        val1 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.value2)
        val2 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        return "Logical("+val1+","+val2+",'"+str(self.type)+"')"
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"' + str(self.type) + '\"]\n'
        try:
            dot += self.value1.graphAST('',hash(self))
            dot += self.value2.graphAST('',hash(self))
        except Exception as e:
            print(e)
        return dot
    def translate(self,opts,indent):
        t1 = self.value1.translate(opts,indent)
        t2 = self.value2.translate(opts,indent)
        code = ""
        diccionario = {}
        diccionario['resultado']=opts.generateTemp()
        if isinstance(t1,Value): 
            diccionario['argumento1']=str(t1.value)
        else: 
            diccionario['argumento1']=inspect.cleandoc(t1.split("\n")[-2].split("=")[0])
            code+=t1
        if isinstance(t2,Value): 
            diccionario['argumento2']=str(t2.value)
        else: 
            diccionario['argumento2']=inspect.cleandoc(t2.split("\n")[-2].split("=")[0])
            code+=t2
        diccionario['operacion']=self.type.lower()
        opts.pila.append(diccionario)
        return code+(indent*"\t")+diccionario['resultado']+"="+diccionario['argumento1']+self.type.lower()+diccionario['argumento2']+"\n"

class Relational(Expression):
    def __init__(self, value1, value2, type):
        self.value1 = value1
        self.value2 = value2
        self.type = type
    def __repr__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.value1)
        val1 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.value2)
        val2 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        return "Relational("+val1+","+val2+",'"+str(self.type)+"')" 
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"' + str(self.type) + '\"]\n'
        dot += self.value1.graphAST('',hash(self))
        dot += self.value2.graphAST('',hash(self))
        return dot
    def translate(self,opts,indent):
        t1 = self.value1.translate(opts,indent)
        t2 = self.value2.translate(opts,indent)
        transtype = self.type
        if self.type == "=": transtype = "=="
        code = ""
        diccionario = {}
        diccionario['resultado']=opts.generateTemp()
        if isinstance(t1,Value): 
            diccionario['argumento1']=str(t1.value)
        else: 
            diccionario['argumento1']=inspect.cleandoc(t1.split("\n")[-2].split("=")[0])
            code+=t1
        if isinstance(t2,Value): 
            diccionario['argumento2']=str(t2.value)
        else: 
            diccionario['argumento2']=inspect.cleandoc(t2.split("\n")[-2].split("=")[0])
            code+=t2
        diccionario['operacion']=transtype
        opts.pila.append(diccionario)
        return code+(indent*"\t")+diccionario['resultado']+"="+diccionario['argumento1']+transtype+diccionario['argumento2']+"\n"

class Unary(Expression):
    def __init__(self, value, type):
        self.value = value
        self.type = type
    def __repr__(self):
        return "Unary("+str(self.value)+",'"+str(self.type)+"')" 
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"' + str(self.type) + '\"]\n'
        dot += self.value.graphAST('',hash(self))
        return dot
    def translate(self,opts,indent):
        t1 = self.value.translate(opts,indent)
        code = ""
        diccionario = {}
        diccionario['resultado']=opts.generateTemp()
        if isinstance(t1,Value): 
            diccionario['argumento1']=str(t1.value)
        else: 
            diccionario['argumento1']=inspect.cleandoc(t1.split("\n")[-2].split("=")[0])
            code+=t1
        diccionario['argumento2']=None
        diccionario['operacion']=self.type
        opts.pila.append(diccionario)
        return code+(indent*"\t")+diccionario['resultado']+"="+self.type+diccionario['argumento1']+"\n"

class MathFunction(Expression):
    def __init__(self, function, expression):
        self.function = function
        self.expression = expression
    def __repr__(self):
        return "MathFunction('"+self.function+"',"+str(self.expression)+")" 
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"' + str(self.function) + '\"]\n'
        if(self.expression!=0): dot += self.expression.graphAST('',hash(self))
        return dot
    def translate(self,opts,indent):
        t1 = self.expression.translate(opts,indent)
        code = ""
        result = ""
        diccionario1 = {}
        diccionario2 = {}
        diccionario3 = {}
        diccionario4 = {}
        if self.function == "ABS":
            diccionario1['resultado']=opts.generateTemp()
            if isinstance(t1,Value): 
                diccionario1['argumento1']=str(t1.value)
            else: 
                diccionario1['argumento1']=inspect.cleandoc(t1.split("\n")[-2].split("=")[0])
                code+=t1
            diccionario1['argumento2']="0"
            diccionario1['operacion']=">"
            opts.pila.append(diccionario1)
            result+=code+(indent*"\t")+diccionario1['resultado']+"="+diccionario1['argumento1']+">0\n"
            diccionario2['resultado']=opts.generateTemp()
            if isinstance(t1,Value): 
                diccionario2['argumento1']=str(t1.value)
            else: 
                diccionario2['argumento1']=inspect.cleandoc(t1.split("\n")[-2].split("=")[0])
                code+=t1
            diccionario2['argumento2']="0"
            diccionario2['operacion']="<"
            opts.pila.append(diccionario2)
            result+=(indent*"\t")+diccionario2['resultado']+"="+diccionario2['argumento1']+"<0\n"
            diccionario3 = {'resultado':opts.generateTemp(),'argumento1':diccionario1['resultado'],'argumento2':diccionario2['resultado'],'operacion':"-"}
            opts.pila.append(diccionario3)
            result+=(indent*"\t")+diccionario3['resultado']+"="+diccionario1['resultado']+"-"+diccionario2['resultado']+"\n"
            diccionario4 = {'resultado':opts.generateTemp(),'argumento1':diccionario1['resultado'],'argumento2':diccionario2['resultado'],'operacion':"-"}
            opts.pila.append(diccionario4)
            result+=(indent*"\t")+diccionario4['resultado']+"="+diccionario1['argumento1']+"*"+diccionario3['resultado']+"\n"
        elif self.function == "CEIL" or self.function == "CEILING":
            diccionario1['resultado']=opts.generateTemp()
            if isinstance(t1,Value): 
                diccionario1['argumento1']=str(t1.value)
            else: 
                diccionario1['argumento1']=inspect.cleandoc(t1.split("\n")[-2].split("=")[0])
                code+=t1
            diccionario1['argumento2']=None
            diccionario1['operacion']="math.ceil"
            opts.pila.append(diccionario1)
            result+=code+(indent*"\t")+diccionario1['resultado']+"=math.ceil("+diccionario1['argumento1']+")\n"
        elif self.function == "CBRT":
            if isinstance(t1,Value): 
                diccionario2['argumento1']=str(t1.value)
            else: 
                diccionario2['argumento1']=inspect.cleandoc(t1.split("\n")[-2].split("=")[0])
                code+=t1
            diccionario1 = {'resultado':opts.generateTemp(),'argumento1':'1','argumento2':"3",'operacion':"/"}
            opts.pila.append(diccionario1)
            result+=code+(indent*"\t")+diccionario1['resultado']+"="+"1/3\n"
            diccionario2['resultado']=opts.generateTemp()
            diccionario2['argumento2']=diccionario1['resultado']
            diccionario2['operacion']="**"
            opts.pila.append(diccionario2)
            print(diccionario1)
            print(diccionario2)
            result+=(indent*"\t")+diccionario2['resultado']+"="+diccionario2['argumento1']+"**"+diccionario2['argumento2']+"\n"
        elif self.function == "SQRT":
            if isinstance(t1,Value): 
                diccionario2['argumento1']=str(t1.value)
            else: 
                diccionario2['argumento1']=inspect.cleandoc(t1.split("\n")[-2].split("=")[0])
                code+=t1
            diccionario1 = {'resultado':opts.generateTemp(),'argumento1':'1','argumento2':"2",'operacion':"/"}
            opts.pila.append(diccionario1)
            result+=code+(indent*"\t")+diccionario1['resultado']+"="+"1/2\n"
            diccionario2['resultado']=opts.generateTemp()
            diccionario2['argumento2']=diccionario1['resultado']
            diccionario2['operacion']="**"
            opts.pila.append(diccionario2)
            result+=(indent*"\t")+diccionario2['resultado']+"="+diccionario1['argumento1']+"**"+diccionario1['resultado']+"\n"
        return result
    

class TrigonometricFunction(Expression):
    def __init__(self, function, expression):
        self.function = function
        self.expression = expression
    def __repr__(self):
        
        return "TrigonometricFunction('"+self.function+"',"+str(self.expression)+")"
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"' + str(self.function) + '\"]\n'
        dot += self.expression.graphAST('',hash(self))
        return dot
    def translate(self,opts,indent):
        t1 = self.expression.translate(opts,indent)
        result = "" #sin sinh acosd
        diccionario1 = {}
        code = ""
        if self.function == "SIN":
            diccionario1['resultado']=opts.generateTemp()
            if isinstance(t1,Value): 
                diccionario1['argumento1']=str(t1.value)
            else: 
                diccionario1['argumento1']=inspect.cleandoc(t1.split("\n")[-2].split("=")[0])
                code+=t1
            diccionario1['argumento2']=None
            diccionario1['operacion']="math.sin"
            opts.pila.append(diccionario1)
            result+=code+(indent*"\t")+diccionario1['resultado']+"=math.sin("+diccionario1['argumento1']+")\n"
        elif self.function == "SINH":
            diccionario1['resultado']=opts.generateTemp()
            if isinstance(t1,Value): 
                diccionario1['argumento1']=str(t1.value)
            else: 
                diccionario1['argumento1']=inspect.cleandoc(t1.split("\n")[-2].split("=")[0])
                code+=t1
            diccionario1['argumento2']=None
            diccionario1['operacion']="math.sinh"
            opts.pila.append(diccionario1)
            result+=code+(indent*"\t")+diccionario1['resultado']+"=math.sinh("+diccionario1['argumento1']+")\n"
        elif self.function == "ACOSD":
            diccionario1['resultado']=opts.generateTemp()
            if isinstance(t1,Value): 
                diccionario1['argumento1']=str(t1.value)
            else: 
                diccionario1['argumento1']=inspect.cleandoc(t1.split("\n")[-2].split("=")[0])
                code+=t1
            diccionario1['argumento2']=None
            diccionario1['operacion']="math.acosd"
            opts.pila.append(diccionario1)
            result+=code+(indent*"\t")+diccionario1['resultado']+"=math.degrees(math.acos("+diccionario1['argumento1']+"))\n"
        return result

class ArgumentListFunction(Expression):
    def __init__(self, function, expressions):
        self.function = function
        self.expressions = expressions
    def __repr__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.expressions)
        exp = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        return "ArgumentListFunction('"+self.function+"',"+str(exp)+")"
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        str(hash("expressions") + hash(self)) + '\n'
        dot += str(hash("expressions") + hash(self)) + \
            '[label=\"' + "expressions" + '\"]\n'
        for expression in self.expressions:
            dot+= expression.graphAST('',str(hash("expressions") + hash(self)))
        return dot
    def translate(self,opts,indent):
        t1 = self.expressions[0].translate(opts,indent)
        result = "" #sin sinh acosd
        if self.function == "TRUNC":
            diccionario1 = {'resultado':opts.generateTemp(),'argumento1':inspect.cleandoc(t1.split("\n")[-2].split("=")[0]),'argumento2':None,'operacion':"math.trunc"}
            opts.pila.append(diccionario1)
            result+=t1+(indent*"\t")+diccionario1['resultado']+"=math.trunc("+diccionario1['argumento1']+")\n"
        return result
        
class AggFunction(Expression):
    def __init__(self, function, expression):
        self.function = function
        self.expression = expression
    def __repr__(self):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.expression)
        exp = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        return "AggFunction('"+self.function+"',"+str(exp)+")"
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"' + str(self.function) + '\"]\n'
        dot += self.expression.graphAST('',hash(self))
        return dot

class ExtractFunction(Expression):
    def __init__(self, function, expression):
        self.function = function
        self.expression = expression
    def __repr__(self):
        
        return "ExtractFunction('"+self.function+"',"+str(self.expression)+")" 
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"' + str(self.function) + '\"]\n'
        dot += self.expression.graphAST('',hash(self))
        return dot
    def translate(self,opts,indent):
        t1 = self.expression.translate(opts,indent)
        result = ""
        return result

class CreatedFunction(Expression):
    def __init__(self, function, expressions):
        self.function = function
        self.expressions = expressions
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        str(hash("expressions") + hash(self)) + '\n'
        dot += str(hash("expressions") + hash(self)) + \
            '[label=\"' + "expressions" + '\"]\n'
        for expression in self.expressions:
            dot+= expression.graphAST('',str(hash("expressions") + hash(self)))
        return dot

class SelectFunction(Expression):
    def __init__(self, select):
        self.select = select
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"' + str("SELECT") + '\"]\n'
        return dot
    def translate(self,opts,indent):
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        print(self.select)
        val1 = new_stdout.getvalue()[:-1]
        sys.stdout = old_stdout
        result = Value(1,val1)
        return result

class ExpressionAsStringFunction(Expression):
    def __init__(self, expression):
        self.expression = expression
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"AS STRING\"]\n'
        dot += self.expression.graphAST('',hash(self))
        return dot

class NSeparator(Expression):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\".\"]\n'
        dot += self.value1.graphAST('',hash(self))
        dot += self.value2.graphAST('',hash(self))
        return dot
class Alias(Expression):
    def __init__(self, expression, alias):
        self.expression = expression
        self.alias = alias
    def __repr__(self):
        
        return "Alias("+str(self.expression)+",'"+str(self.alias)+"')" 
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"AS ' + str(self.alias) + '\"]\n'
        dot += self.expression.graphAST('',hash(self))
        return dot

class DatePartFunction(Expression):
    def __init__(self, function, expression):
        self.function = function
        self.expression = expression
    def __repr__(self):

        return "DatePartFunction('"+str(self.function)+"',"+str(self.expression)+")" 
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"' + str(self.function) + '\"]\n'
        dot += self.expression.graphAST('',hash(self))
        return dot

class CountFunction(Expression):
    def __init__(self, function):
        self.function = function
    def __repr__(self):
        v=str(self.function)
        return "CountFunction('"+v+"')"
    def graphAST(self, dot, parent):
        dot += str(parent) + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"' + str(self.function) + '\"]\n'
        #dot += self.expression.graphAST('',hash(self))
        return dot