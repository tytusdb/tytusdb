from analizer.abstract.expression import Expression
from analizer.abstract.expression import TYPE
from analizer.statement.expressions import code


class Ternary(Expression):


    def __init__(self,temp , exp1, exp2, exp3, operator, row, column):
        super().__init__(row, column)
        self.temp = int(temp)-1
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.operator = operator


    def execute(self, environment):
        exp1 = self.exp1.execute(environment)
        exp2 = self.exp2.execute(environment)
        exp3 = self.exp3.execute(environment)
        operator = self.operator

        if operator == "BETWEEN":
            exp1_ = Binary(self.newTemp(),exp1,exp2,">",self.row,self.column)
            exp2_ = Binary(self.newTemp(),exp1,exp3,"<",self.row,self.column)
            return Binary(self.newTemp(),exp1_,exp2_,"AND",self.row,self.column).execute(environment)
        elif operator == "NOTBETWEEN":
            exp1_ = Binary(self.newTemp(),exp1,exp2,">",self.row,self.column)
            exp2_ = Binary(self.newTemp(),exp1,exp3,"<",self.row,self.column)
            exp3 = Binary(self.newTemp(),exp1_,exp2_,"AND",self.row,self.column)
            return Unary(self.newTemp(),exp3,"NOT",self.row,self.column).execute(environment)
        else : #operator == "BETWEENSYMMETRIC"
            exp4 = Binary(self.newTemp(),exp1,exp2,">",self.row,self.column)
            exp5 = Binary(self.newTemp(),exp1,exp3,"<",self.row,self.column)
            exp6 = Binary(self.newTemp(),exp4,exp5,"AND",self.row,self.column)
            exp4 = Binary(self.newTemp(),exp1,exp2,"<",self.row,self.column)
            exp5 = Binary(self.newTemp(),exp1,exp3,">",self.row,self.column)
            exp7 = Binary(self.newTemp(),exp4,exp5,"AND",self.row,self.column)
            return Binary(self.newTemp(),exp6,exp7,"OR",self.row,self.column).execute(environment)


    def newTemp(self):
        self.temp += 1
        return str(self.temp)

class Binary(Expression):
    """
    Esta clase recibe dos parametros de expresion
    para realizar el  C3D
    """

    def __init__(self,temp, exp1, exp2, operator, row, column):
        super().__init__(row, column)
        self.temp = "t"+temp
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator

    def execute(self, environment):
        exp1 = self.exp1.execute(environment)
        exp2 = self.exp2.execute(environment)
        exp = exp1.value + exp2.value + self.temp + " = " + str(exp1.temp) +" " + self.operator.lower() + " "+ str(exp2.temp) + "\n"
        return code.C3D(exp, self.temp, self.row, self.column)

class Unary(Expression):
    """
    Esta clase recibe un parametro de expresion
    para realizar el  C3D
    """

    def __init__(self,temp, exp, operator, row, column):
        super().__init__(row, column)
        self.temp = "t"+temp
        self.exp = exp
        self.operator = operator

    def execute(self, environment):
        exp = self.exp.execute(environment)
        if self.operator == "+":
            exp = exp.value + self.temp + " = " + str(exp.temp)+ "\n"
        elif self.operator == "-":
            exp = exp.value + self.temp + " = -1 * " + str(exp.temp)+ "\n"
        elif self.operator == "NOTNULL":
            exp = exp.value + self.temp + " = " + str(exp.temp)+ " != NULL" + "\n"
        elif self.operator == "NOT":
            exp = exp.value + self.temp + " = not " + str(exp.temp)+ "\n"
        else:
            if "NOT" in self.operator:                
                exp2 = self.operator[5:]
                self.operator = " != "
                
            else:                
                exp2 = self.operator[2:]
                self.operator = " == "
            exp = exp.value + self.temp + " = " + str(exp.temp)+ self.operator + exp2 + "\n"
        return code.C3D(exp,self.temp,self.row,self.column)
